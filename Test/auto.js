/** @param {NS} ns */
export async function main(ns) {
    const HACK_SCRIPT = '/scripts/hack.js';
    const GROW_SCRIPT = '/scripts/grow.js';
    const WEAKEN_SCRIPT = '/scripts/weaken.js';
    
    // Create basic scripts if they don't exist
    await setupScripts(ns);
    
    ns.tprint('Starting automation...');
    
    while (true) {
        // 1. Scan network and root all accessible servers
        const servers = scanNetwork(ns);
        await rootServers(ns, servers);
        
        // 2. Find best target
        const target = findBestTarget(ns, servers);
        if (target) {
            ns.tprint(`Best target: ${target}`);
            
            // 3. Deploy scripts to all servers
            await deployScripts(ns, servers, target);
        }
        
        // 4. Purchase new servers if we can afford them
        await purchaseServers(ns);
        
        // 5. Upgrade home RAM if possible
        await upgradeHome(ns);
        
        // Wait before next cycle
        await ns.sleep(60000); // Check every minute
    }
}

function scanNetwork(ns) {
    const visited = new Set();
    const servers = [];
    
    function scan(server) {
        if (visited.has(server)) return;
        visited.add(server);
        servers.push(server);
        
        const connections = ns.scan(server);
        for (const connected of connections) {
            scan(connected);
        }
    }
    
    scan('home');
    return servers;
}

async function rootServers(ns, servers) {
    let newRoots = 0;
    
    for (const server of servers) {
        if (ns.hasRootAccess(server)) continue;
        
        const portsNeeded = ns.getServerNumPortsRequired(server);
        let portsOpened = 0;
        
        // Try all port openers
        if (ns.fileExists('BruteSSH.exe', 'home')) {
            ns.brutessh(server);
            portsOpened++;
        }
        if (ns.fileExists('FTPCrack.exe', 'home')) {
            ns.ftpcrack(server);
            portsOpened++;
        }
        if (ns.fileExists('relaySMTP.exe', 'home')) {
            ns.relaysmtp(server);
            portsOpened++;
        }
        if (ns.fileExists('HTTPWorm.exe', 'home')) {
            ns.httpworm(server);
            portsOpened++;
        }
        if (ns.fileExists('SQLInject.exe', 'home')) {
            ns.sqlinject(server);
            portsOpened++;
        }
        
        // Try to nuke if we have enough ports
        if (portsOpened >= portsNeeded) {
            try {
                ns.nuke(server);
                newRoots++;
                ns.tprint(`✓ Rooted ${server}`);
            } catch (e) {
                // Can't root yet
            }
        }
    }
    
    if (newRoots > 0) {
        ns.tprint(`Gained root on ${newRoots} new servers!`);
    }
}

function findBestTarget(ns, servers) {
    let bestTarget = null;
    let bestScore = 0;
    
    const hackLevel = ns.getHackingLevel();
    
    for (const server of servers) {
        if (!ns.hasRootAccess(server)) continue;
        if (ns.getServerRequiredHackingLevel(server) > hackLevel) continue;
        
        const maxMoney = ns.getServerMaxMoney(server);
        if (maxMoney === 0) continue;
        
        const minSec = ns.getServerMinSecurityLevel(server);
        const growthRate = ns.getServerGrowth(server);
        
        // Score based on money and ease of hacking
        const score = (maxMoney / minSec) * growthRate;
        
        if (score > bestScore) {
            bestScore = score;
            bestTarget = server;
        }
    }
    
    return bestTarget;
}

async function deployScripts(ns, servers, target) {
    const scripts = [
        { file: '/scripts/hack.js', ram: 1.7 },
        { file: '/scripts/grow.js', ram: 1.75 },
        { file: '/scripts/weaken.js', ram: 1.75 }
    ];
    
    for (const server of servers) {
        if (!ns.hasRootAccess(server)) continue;
        if (server === 'home' && ns.getServerMaxRam('home') < 32) continue; // Keep home for running this script
        
        const maxRam = ns.getServerMaxRam(server);
        if (maxRam === 0) continue;
        
        // Kill existing scripts
        ns.killall(server);
        
        // Copy scripts
        for (const script of scripts) {
            await ns.scp(script.file, server, 'home');
        }
        
        const availableRam = maxRam - ns.getServerUsedRam(server);
        
        // Calculate how many threads we can run
        const hackThreads = Math.floor(availableRam / (scripts[0].ram * 3));
        const growThreads = Math.floor(availableRam / (scripts[1].ram * 3));
        const weakenThreads = Math.floor(availableRam / (scripts[2].ram * 3));
        
        // Start scripts
        if (hackThreads > 0) {
            ns.exec('/scripts/hack.js', server, hackThreads, target);
        }
        if (growThreads > 0) {
            ns.exec('/scripts/grow.js', server, growThreads, target);
        }
        if (weakenThreads > 0) {
            ns.exec('/scripts/weaken.js', server, weakenThreads, target);
        }
    }
}

async function purchaseServers(ns) {
    const maxServers = ns.getPurchasedServerLimit();
    const ownedServers = ns.getPurchasedServers();
    
    if (ownedServers.length >= maxServers) return;
    
    const ram = 8; // Start with 8GB
    const cost = ns.getPurchasedServerCost(ram);
    
    if (ns.getServerMoneyAvailable('home') > cost * 2) {
        const hostname = ns.purchaseServer(`pserv-${ownedServers.length}`, ram);
        if (hostname) {
            ns.tprint(`✓ Purchased server: ${hostname} (${ram}GB)`);
        }
    }
}

async function upgradeHome(ns) {
    // Try to upgrade home RAM
    const currentRam = ns.getServerMaxRam('home');
    if (ns.singularity && ns.singularity.upgradeHomeRam) {
        const cost = ns.singularity.getUpgradeHomeRamCost();
        if (ns.getServerMoneyAvailable('home') > cost * 10) {
            if (ns.singularity.upgradeHomeRam()) {
                ns.tprint(`✓ Upgraded home RAM to ${currentRam * 2}GB`);
            }
        }
    }
}

async function setupScripts(ns) {
    // Create hack script
    const hackScript = `/** @param {NS} ns */
export async function main(ns) {
    const target = ns.args[0];
    while (true) {
        await ns.hack(target);
    }
}`;
    
    // Create grow script
    const growScript = `/** @param {NS} ns */
export async function main(ns) {
    const target = ns.args[0];
    while (true) {
        await ns.grow(target);
    }
}`;
    
    // Create weaken script
    const weakenScript = `/** @param {NS} ns */
export async function main(ns) {
    const target = ns.args[0];
    while (true) {
        await ns.weaken(target);
    }
}`;
    
    await ns.write('/scripts/hack.js', hackScript, 'w');
    await ns.write('/scripts/grow.js', growScript, 'w');
    await ns.write('/scripts/weaken.js', weakenScript, 'w');
}
