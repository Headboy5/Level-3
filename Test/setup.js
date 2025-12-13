/** @param {NS} ns */
// Setup script - Creates all necessary automation files
export async function main(ns) {
    ns.tprint('==========================================');
    ns.tprint('Starting setup...');
    ns.tprint('==========================================');
    ns.disableLog('ALL');
    
    try {
        // Create auto-root script
        ns.tprint('\n[1/11] Creating auto-root.js...');
        const autoRootScript = `/** @param {NS} ns */
// RAM Cost: ~2.5GB - Automatically roots all accessible servers
export async function main(ns) {
    const servers = scanNetwork(ns);
    let newRoots = 0;
    
    for (const server of servers) {
        if (ns.hasRootAccess(server)) continue;
        
        const portsNeeded = ns.getServerNumPortsRequired(server);
        let portsOpened = 0;
        
        // Try all port openers
        try { if (ns.fileExists('BruteSSH.exe', 'home')) { ns.brutessh(server); portsOpened++; } } catch (e) {}
        try { if (ns.fileExists('FTPCrack.exe', 'home')) { ns.ftpcrack(server); portsOpened++; } } catch (e) {}
        try { if (ns.fileExists('relaySMTP.exe', 'home')) { ns.relaysmtp(server); portsOpened++; } } catch (e) {}
        try { if (ns.fileExists('HTTPWorm.exe', 'home')) { ns.httpworm(server); portsOpened++; } } catch (e) {}
        try { if (ns.fileExists('SQLInject.exe', 'home')) { ns.sqlinject(server); portsOpened++; } } catch (e) {}
        
        // Try to nuke if we have enough ports
        if (portsOpened >= portsNeeded) {
            try {
                ns.nuke(server);
                newRoots++;
                ns.tprint('✓ Rooted ' + server);
            } catch (e) {}
        }
    }
    
    ns.tprint('Total: ' + servers.length + ' servers, ' + newRoots + ' newly rooted');
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
}`;
        
        // Create find-target script
        ns.tprint('[2/11] Creating find-target.js...');
        const findTargetScript = `/** @param {NS} ns */
// RAM Cost: ~2.0GB - Finds the best target server to hack
export async function main(ns) {
    const servers = scanNetwork(ns);
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
    
    if (bestTarget) {
        ns.tprint('Best target: ' + bestTarget);
        ns.tprint('  Max money: $' + ns.formatNumber(ns.getServerMaxMoney(bestTarget)));
        ns.tprint('  Required level: ' + ns.getServerRequiredHackingLevel(bestTarget));
        ns.tprint('  Min security: ' + ns.getServerMinSecurityLevel(bestTarget));
        await ns.writePort(1, bestTarget);
    } else {
        ns.tprint('No suitable targets found');
        await ns.writePort(1, null);
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
}`;
        
        // Create deploy script
        ns.tprint('[3/11] Creating deploy.js...');
        const deployScript = `/** @param {NS} ns */
// RAM Cost: ~3.5GB - Deploys hack script to all servers targeting specified server
export async function main(ns) {
    if (ns.args.length === 0) {
        ns.tprint('Usage: run deploy.js [target]');
        ns.tprint('Example: run deploy.js n00dles');
        return;
    }
    
    const target = ns.args[0];
    const servers = scanNetwork(ns);
    
    // Create simple hack script
    const hackScript = '/** @param {NS} ns */\\nexport async function main(ns) {\\n    const target = ns.args[0];\\n    while (true) {\\n        await ns.hack(target);\\n    }\\n}';
    
    await ns.write('/tmp/hack.js', hackScript, 'w');
    
    let deployed = 0;
    for (const server of servers) {
        if (!ns.hasRootAccess(server)) continue;
        
        const maxRam = ns.getServerMaxRam(server);
        if (maxRam < 2) continue;
        
        // Copy and run
        await ns.scp('/tmp/hack.js', server, 'home');
        ns.killall(server);
        
        const threads = Math.floor((maxRam - 1) / 1.7);
        if (threads > 0) {
            ns.exec('/tmp/hack.js', server, threads, target);
            deployed++;
        }
    }
    
    ns.tprint('✓ Deployed to ' + deployed + ' servers targeting ' + target);
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
}`;
        
        // Create simple-hack script
        ns.tprint('[4/11] Creating simple-hack.js...');
        const simpleHackScript = `/** @param {NS} ns */
// RAM Cost: ~1.7GB - Simple hack script
export async function main(ns) {
    const target = ns.args[0] || 'n00dles';
    
    while (true) {
        await ns.hack(target);
    }
}`;
        
        // Create simple-grow script
        ns.tprint('[5/11] Creating simple-grow.js...');
        const simpleGrowScript = `/** @param {NS} ns */
// RAM Cost: ~1.75GB - Simple grow script
export async function main(ns) {
    const target = ns.args[0] || 'n00dles';
    
    while (true) {
        await ns.grow(target);
    }
}`;
        
        // Create simple-weaken script
        ns.tprint('[6/11] Creating simple-weaken.js...');
        const simpleWeakenScript = `/** @param {NS} ns */
// RAM Cost: ~1.75GB - Simple weaken script
export async function main(ns) {
    const target = ns.args[0] || 'n00dles';
    
    while (true) {
        await ns.weaken(target);
    }
}`;
        
        // Create auto-lite script
        ns.tprint('[7/11] Creating auto-lite.js...');
        const autoLiteScript = `/** @param {NS} ns */
// RAM Cost: ~6.0GB - Runs auto-root and deploy in a loop
export async function main(ns) {
    ns.tprint('Starting lite automation...');
    
    while (true) {
        // Root servers
        ns.tprint('--- Rooting servers ---');
        await ns.run('auto-root.js');
        await ns.sleep(5000);
        
        // Find target
        ns.tprint('--- Finding best target ---');
        await ns.run('find-target.js');
        await ns.sleep(2000);
        
        // Deploy (you need to set target manually for now)
        const target = ns.args[0] || 'n00dles';
        ns.tprint('--- Deploying scripts to target: ' + target + ' ---');
        await ns.run('deploy.js', 1, target);
        await ns.sleep(5000);
        
        // Wait before next cycle
        ns.tprint('Waiting 5 minutes before next cycle...');
        await ns.sleep(300000); // 5 minutes
    }
}`;
        
        // Write all files
        ns.tprint('\n==========================================');
        ns.tprint('Writing files to disk...');
        ns.tprint('==========================================\n');
        
        await ns.write('auto-root.js', autoRootScript, 'w');
        ns.tprint('✓ Created auto-root.js (' + autoRootScript.length + ' bytes)');
        await ns.sleep(100);
        
        await ns.write('find-target.js', findTargetScript, 'w');
        ns.tprint('✓ Created find-target.js (' + findTargetScript.length + ' bytes)');
        await ns.sleep(100);
        
        await ns.write('deploy.js', deployScript, 'w');
        ns.tprint('✓ Created deploy.js (' + deployScript.length + ' bytes)');
        await ns.sleep(100);
        
        await ns.write('simple-hack.js', simpleHackScript, 'w');
        ns.tprint('✓ Created simple-hack.js (' + simpleHackScript.length + ' bytes)');
        await ns.sleep(100);
        
        await ns.write('simple-grow.js', simpleGrowScript, 'w');
        ns.tprint('✓ Created simple-grow.js (' + simpleGrowScript.length + ' bytes)');
        await ns.sleep(100);
        
        await ns.write('simple-weaken.js', simpleWeakenScript, 'w');
        ns.tprint('✓ Created simple-weaken.js (' + simpleWeakenScript.length + ' bytes)');
        await ns.sleep(100);
        
        await ns.write('auto-lite.js', autoLiteScript, 'w');
        ns.tprint('✓ Created auto-lite.js (' + autoLiteScript.length + ' bytes)');
        await ns.sleep(100);
        
        // Create smart-deploy script
        ns.tprint('[8/11] Creating smart-deploy.js...');
        const smartDeployScript = '/** @param {NS} ns */\\n// RAM Cost: ~4.5GB - Intelligently deploys scripts with calculated thread ratios\\nexport async function main(ns) {\\n    let target = ns.args[0];\\n    if (!target) {\\n        ns.tprint(\\\'No target specified, finding best target...\\\');\\n        ns.run(\\\'find-target.js\\\');\\n        await ns.sleep(2000);\\n        target = ns.readPort(1);\\n        if (target === \\\'NULL PORT DATA\\\' || !target) {\\n            const servers = scanNetwork(ns);\\n            for (const server of servers) {\\n                if (ns.hasRootAccess(server) && ns.getServerMaxMoney(server) > 0) {\\n                    target = server;\\n                    break;\\n                }\\n            }\\n        }\\n        if (!target) {\\n            ns.tprint(\\\'ERROR: No suitable target found!\\\');\\n            return;\\n        }\\n        ns.tprint(\\\'Auto-selected target: \\\' + target);\\n    }\\n    const servers = scanNetwork(ns);\\n    const hackScript = \\\'/** @param {NS} ns */\\\\nexport async function main(ns) {\\\\n    const target = ns.args[0];\\\\n    while (true) {\\\\n        await ns.hack(target);\\\\n    }\\\\n}\\\';\\n    const growScript = \\\'/** @param {NS} ns */\\\\nexport async function main(ns) {\\\\n    const target = ns.args[0];\\\\n    while (true) {\\\\n        await ns.grow(target);\\\\n    }\\\\n}\\\';\\n    const weakenScript = \\\'/** @param {NS} ns */\\\\nexport async function main(ns) {\\\\n    const target = ns.args[0];\\\\n    while (true) {\\\\n        await ns.weaken(target);\\\\n    }\\\\n}\\\';\\n    await ns.write(\\\'/tmp/hack.js\\\', hackScript, \\\'w\\\');\\n    await ns.write(\\\'/tmp/grow.js\\\', growScript, \\\'w\\\');\\n    await ns.write(\\\'/tmp/weaken.js\\\', weakenScript, \\\'w\\\');\\n    const hackRam = ns.getScriptRam(\\\'/tmp/hack.js\\\');\\n    const growRam = ns.getScriptRam(\\\'/tmp/grow.js\\\');\\n    const weakenRam = ns.getScriptRam(\\\'/tmp/weaken.js\\\');\\n    const currentSecurity = ns.getServerSecurityLevel(target);\\n    const minSecurity = ns.getServerMinSecurityLevel(target);\\n    const currentMoney = ns.getServerMoneyAvailable(target);\\n    const maxMoney = ns.getServerMaxMoney(target);\\n    const securityDiff = currentSecurity - minSecurity;\\n    const moneyPercent = maxMoney > 0 ? currentMoney / maxMoney : 0;\\n    ns.tprint(\\\'=== Target Analysis ===\\\');\\n    ns.tprint(\\\'Server: \\\' + target);\\n    ns.tprint(\\\'Security: \\\' + currentSecurity.toFixed(2) + \\\' / \\\' + minSecurity.toFixed(2) + \\\' (diff: \\\' + securityDiff.toFixed(2) + \\\')\\\');\\n    ns.tprint(\\\'Money: $\\\' + ns.formatNumber(currentMoney) + \\\' / $\\\' + ns.formatNumber(maxMoney) + \\\' (\\\' + (moneyPercent * 100).toFixed(1) + \\\'%)\\\');\\n    let weakenRatio, growRatio, hackRatio;\\n    if (securityDiff > 5) {\\n        weakenRatio = 0.70;\\n        growRatio = 0.25;\\n        hackRatio = 0.05;\\n        ns.tprint(\\\'Strategy: WEAKEN-HEAVY (high security)\\\');\\n    } else if (moneyPercent < 0.5) {\\n        weakenRatio = 0.40;\\n        growRatio = 0.50;\\n        hackRatio = 0.10;\\n        ns.tprint(\\\'Strategy: GROW-HEAVY (low money)\\\');\\n    } else if (moneyPercent < 0.75) {\\n        weakenRatio = 0.45;\\n        growRatio = 0.40;\\n        hackRatio = 0.15;\\n        ns.tprint(\\\'Strategy: BALANCED-GROW\\\');\\n    } else {\\n        weakenRatio = 0.50;\\n        growRatio = 0.30;\\n        hackRatio = 0.20;\\n        ns.tprint(\\\'Strategy: NORMAL OPERATION\\\');\\n    }\\n    let deployed = 0;\\n    let totalWeaken = 0, totalGrow = 0, totalHack = 0;\\n    for (const server of servers) {\\n        if (!ns.hasRootAccess(server)) continue;\\n        const maxRam = ns.getServerMaxRam(server);\\n        if (maxRam < 2) continue;\\n        await ns.scp(\\\'/tmp/hack.js\\\', server, \\\'home\\\');\\n        await ns.scp(\\\'/tmp/grow.js\\\', server, \\\'home\\\');\\n        await ns.scp(\\\'/tmp/weaken.js\\\', server, \\\'home\\\');\\n        ns.killall(server);\\n        let availableRam = maxRam - ns.getServerUsedRam(server);\\n        if (server === \\\'home\\\') {\\n            availableRam = Math.max(0, availableRam - 50);\\n        }\\n        if (availableRam < Math.min(hackRam, growRam, weakenRam)) continue;\\n        const totalPossibleThreads = Math.floor(availableRam / ((weakenRatio * weakenRam) + (growRatio * growRam) + (hackRatio * hackRam)));\\n        const weakenThreads = Math.max(1, Math.floor(totalPossibleThreads * weakenRatio));\\n        const growThreads = Math.max(1, Math.floor(totalPossibleThreads * growRatio));\\n        const hackThreads = Math.max(1, Math.floor(totalPossibleThreads * hackRatio));\\n        const neededRam = (weakenThreads * weakenRam) + (growThreads * growRam) + (hackThreads * hackRam);\\n        if (neededRam > availableRam) {\\n            const scale = availableRam / neededRam;\\n            const adjustedWeaken = Math.floor(weakenThreads * scale);\\n            const adjustedGrow = Math.floor(growThreads * scale);\\n            const adjustedHack = Math.floor(hackThreads * scale);\\n            if (adjustedWeaken > 0) ns.exec(\\\'/tmp/weaken.js\\\', server, adjustedWeaken, target);\\n            if (adjustedGrow > 0) ns.exec(\\\'/tmp/grow.js\\\', server, adjustedGrow, target);\\n            if (adjustedHack > 0) ns.exec(\\\'/tmp/hack.js\\\', server, adjustedHack, target);\\n            totalWeaken += adjustedWeaken;\\n            totalGrow += adjustedGrow;\\n            totalHack += adjustedHack;\\n        } else {\\n            if (weakenThreads > 0) ns.exec(\\\'/tmp/weaken.js\\\', server, weakenThreads, target);\\n            if (growThreads > 0) ns.exec(\\\'/tmp/grow.js\\\', server, growThreads, target);\\n            if (hackThreads > 0) ns.exec(\\\'/tmp/hack.js\\\', server, hackThreads, target);\\n            totalWeaken += weakenThreads;\\n            totalGrow += growThreads;\\n            totalHack += hackThreads;\\n        }\\n        deployed++;\\n    }\\n    ns.tprint(\\\'\\\\n=== Deployment Summary ===\\\');\\n    ns.tprint(\\\'Deployed to \\\' + deployed + \\\' servers\\\');\\n    ns.tprint(\\\'Total threads: Weaken=\\\' + totalWeaken + \\\', Grow=\\\' + totalGrow + \\\', Hack=\\\' + totalHack);\\n}\\nfunction scanNetwork(ns) {\\n    const visited = new Set();\\n    const servers = [];\\n    function scan(server) {\\n        if (visited.has(server)) return;\\n        visited.add(server);\\n        servers.push(server);\\n        const connections = ns.scan(server);\\n        for (const connected of connections) {\\n            scan(connected);\\n        }\\n    }\\n    scan(\\\'home\\\');\\n    return servers;\\n}';
        await ns.write('smart-deploy.js', smartDeployScript, 'w');
        ns.tprint('✓ Created smart-deploy.js (' + smartDeployScript.length + ' bytes)');
        await ns.sleep(100);
        
        // Create buy-servers script
        ns.tprint('[9/11] Creating buy-servers.js...');
        const buyServersScript = '/** @param {NS} ns */\\n// RAM Cost: ~5.0GB - Automatically purchases and upgrades servers\\nexport async function main(ns) {\\n    ns.disableLog(\\\'ALL\\\');\\n    const maxServers = ns.getPurchasedServerLimit();\\n    const currentServers = ns.getPurchasedServers();\\n    ns.tprint(\\\'=== Server Purchase Manager ===\\\');\\n    ns.tprint(\\\'Current servers: \\\' + currentServers.length + \\\' / \\\' + maxServers);\\n    ns.tprint(\\\'Available money: $\\\' + ns.formatNumber(ns.getServerMoneyAvailable(\\\'home\\\')));\\n    const ramTiers = [8, 16, 32, 64, 128, 256, 512, 1024];\\n    if (currentServers.length < maxServers) {\\n        ns.tprint(\\\'\\\\n--- Buying New Servers ---\\\');\\n        for (let i = currentServers.length; i < maxServers; i++) {\\n            let buyRam = 8;\\n            for (const ram of ramTiers) {\\n                const cost = ns.getPurchasedServerCost(ram);\\n                if (ns.getServerMoneyAvailable(\\\'home\\\') >= cost * 1.5) {\\n                    buyRam = ram;\\n                } else {\\n                    break;\\n                }\\n            }\\n            const cost = ns.getPurchasedServerCost(buyRam);\\n            const money = ns.getServerMoneyAvailable(\\\'home\\\');\\n            if (money >= cost * 1.5) {\\n                const hostname = ns.purchaseServer(\\\'pserv-\\\' + i, buyRam);\\n                if (hostname) {\\n                    ns.tprint(\\\'✓ Purchased: \\\' + hostname + \\\' with \\\' + buyRam + \\\'GB RAM ($\\\' + ns.formatNumber(cost) + \\\')\\\');\\n                } else {\\n                    ns.tprint(\\\'✗ Failed to purchase server\\\');\\n                    break;\\n                }\\n            } else {\\n                ns.tprint(\\\'Not enough money for more servers (need $\\\' + ns.formatNumber(cost * 1.5) + \\\')\\\');\\n                break;\\n            }\\n        }\\n    }\\n    ns.tprint(\\\'\\\\n--- Checking Upgrades ---\\\');\\n    for (const server of currentServers) {\\n        const currentRam = ns.getServerMaxRam(server);\\n        let nextRam = null;\\n        for (const ram of ramTiers) {\\n            if (ram > currentRam) {\\n                nextRam = ram;\\n                break;\\n            }\\n        }\\n        if (!nextRam) {\\n            ns.tprint(\\\'✓ \\\' + server + \\\' already at max (\\\' + currentRam + \\\'GB)\\\');\\n            continue;\\n        }\\n        const upgradeCost = ns.getPurchasedServerCost(nextRam);\\n        const money = ns.getServerMoneyAvailable(\\\'home\\\');\\n        if (money >= upgradeCost * 2) {\\n            const serverId = server.split(\\\'-\\\')[1];\\n            ns.killall(server);\\n            ns.deleteServer(server);\\n            const hostname = ns.purchaseServer(\\\'pserv-\\\' + serverId, nextRam);\\n            if (hostname) {\\n                ns.tprint(\\\'✓ Upgraded \\\' + server + \\\': \\\' + currentRam + \\\'GB → \\\' + nextRam + \\\'GB ($\\\' + ns.formatNumber(upgradeCost) + \\\')\\\');\\n            } else {\\n                ns.tprint(\\\'✗ Failed to upgrade \\\' + server);\\n            }\\n        } else {\\n            ns.tprint(\\\'• \\\' + server + \\\': \\\' + currentRam + \\\'GB (upgrade to \\\' + nextRam + \\\'GB costs $\\\' + ns.formatNumber(upgradeCost) + \\\')\\\');\\n        }\\n    }\\n    ns.tprint(\\\'\\\\n=== Summary ===\\\');\\n    const updatedServers = ns.getPurchasedServers();\\n    let totalRam = 0;\\n    for (const server of updatedServers) {\\n        totalRam += ns.getServerMaxRam(server);\\n    }\\n    ns.tprint(\\\'Total servers: \\\' + updatedServers.length);\\n    ns.tprint(\\\'Total RAM: \\\' + totalRam + \\\'GB\\\');\\n    ns.tprint(\\\'Remaining money: $\\\' + ns.formatNumber(ns.getServerMoneyAvailable(\\\'home\\\')));\\n    if (ns.args[0] === \\\'deploy\\\' && ns.args[1]) {\\n        ns.tprint(\\\'\\\\n--- Auto-deploying to \\\' + ns.args[1] + \\\' ---\\\');\\n        await ns.sleep(1000);\\n        ns.run(\\\'smart-deploy.js\\\', 1, ns.args[1]);\\n    }\\n}';
        await ns.write('buy-servers.js', buyServersScript, 'w');
        ns.tprint('✓ Created buy-servers.js (' + buyServersScript.length + ' bytes)');
        await ns.sleep(100);
        
        // Create faction-work script
        ns.tprint('[10/11] Creating faction-work.js...');
        const factionWorkScript = '/** @param {NS} ns */\\n// RAM Cost: ~2.0GB - Does faction work with unused home RAM\\nexport async function main(ns) {\\n    ns.disableLog(\\\'ALL\\\');\\n    const faction = ns.args[0];\\n    if (!faction) {\\n        ns.tprint(\\\'Usage: run faction-work.js [faction-name] [work-type]\\\');\\n        ns.tprint(\\\'Work types: hacking, field, security\\\');\\n        ns.tprint(\\\'Example: run faction-work.js "CyberSec" hacking\\\');\\n        return;\\n    }\\n    const workType = ns.args[1] || \\\'hacking\\\';\\n    ns.tprint(\\\'=== Faction Work Manager ===\\\');\\n    ns.tprint(\\\'Faction: \\\' + faction);\\n    ns.tprint(\\\'Work type: \\\' + workType);\\n    const homeMaxRam = ns.getServerMaxRam(\\\'home\\\');\\n    const homeUsedRam = ns.getServerUsedRam(\\\'home\\\');\\n    const homeFreeRam = homeMaxRam - homeUsedRam;\\n    ns.tprint(\\\'Home RAM: \\\' + homeUsedRam.toFixed(2) + \\\'GB / \\\' + homeMaxRam + \\\'GB\\\');\\n    ns.tprint(\\\'Free RAM: \\\' + homeFreeRam.toFixed(2) + \\\'GB\\\');\\n    if (homeFreeRam >= 50) {\\n        ns.tprint(\\\'\\\\n⚠ You have \\\' + homeFreeRam.toFixed(0) + \\\'GB free on home!\\\');\\n        ns.tprint(\\\'Consider running: run smart-deploy.js\\\');\\n        ns.tprint(\\\'This will use that RAM for hacking scripts.\\\');\\n    }\\n    ns.tprint(\\\'\\\\nStarting faction work...\\\');\\n    try {\\n        if (workType === \\\'hacking\\\') {\\n            const success = ns.singularity.workForFaction(faction, \\\'hacking\\\', false);\\n            if (success) {\\n                ns.tprint(\\\'✓ Started hacking work for \\\' + faction);\\n            } else {\\n                ns.tprint(\\\'✗ Failed to start faction work (do you have Singularity API access?)\\\');\\n            }\\n        } else if (workType === \\\'field\\\') {\\n            const success = ns.singularity.workForFaction(faction, \\\'field\\\', false);\\n            if (success) {\\n                ns.tprint(\\\'✓ Started field work for \\\' + faction);\\n            } else {\\n                ns.tprint(\\\'✗ Failed to start faction work\\\');\\n            }\\n        } else if (workType === \\\'security\\\') {\\n            const success = ns.singularity.workForFaction(faction, \\\'security\\\', false);\\n            if (success) {\\n                ns.tprint(\\\'✓ Started security work for \\\' + faction);\\n            } else {\\n                ns.tprint(\\\'✗ Failed to start faction work\\\');\\n            }\\n        }\\n    } catch (e) {\\n        ns.tprint(\\\'✗ ERROR: \\\' + e);\\n        ns.tprint(\\\'\\\\nNote: Faction work requires Singularity API (Source-File 4)\\\');\\n        ns.tprint(\\\'If you don\\\\\\\'t have it yet, faction work must be done manually.\\\');\\n    }\\n    ns.tprint(\\\'\\\\n=== Tip ===\\\');\\n    ns.tprint(\\\'Run smart-deploy.js to automatically use free RAM for money-making!\\\');\\n}';
        await ns.write('faction-work.js', factionWorkScript, 'w');
        ns.tprint('✓ Created faction-work.js (' + factionWorkScript.length + ' bytes)');
        await ns.sleep(100);
        
        // Create alias setup script
        ns.tprint('\n[11/11] Creating aliases.js...');
        const aliasesScript = `/** @param {NS} ns */
// Creates aliases for all automation scripts
export async function main(ns) {
    ns.tprint('Setting up aliases...');
    ns.tprint('Run these commands in your terminal:');
    ns.tprint('');
    ns.tprint('alias deploy="run deploy.js"');
    ns.tprint('alias smart="run smart-deploy.js"');
    ns.tprint('alias root="run auto-root.js"');
    ns.tprint('alias target="run find-target.js"');
    ns.tprint('alias lite="run auto-lite.js"');
    ns.tprint('alias buy="run buy-servers.js"');
    ns.tprint('alias faction="run faction-work.js"');
    ns.tprint('alias setup="run setup.js"');
    ns.tprint('alias hack="run simple-hack.js"');
    ns.tprint('alias grow="run simple-grow.js"');
    ns.tprint('alias weaken="run simple-weaken.js"');
    ns.tprint('alias export="run export_network.js"');
    ns.tprint('');
    ns.tprint('After setting aliases, you can use:');
    ns.tprint('  smart          (Auto-deploy with smart thread allocation)');
    ns.tprint('  buy deploy     (Buy servers and deploy)');
    ns.tprint('  faction "CyberSec" hacking');
    ns.tprint('  root');
    ns.tprint('  target');
}`;
        await ns.write('aliases.js', aliasesScript, 'w');
        ns.tprint('✓ Created aliases.js (' + aliasesScript.length + ' bytes)');

        ns.tprint('\n===========================================');
        ns.tprint('✓ SUCCESS! All scripts created!');
        ns.tprint('===========================================');
        ns.tprint('\nTo set up aliases, run:');
        ns.tprint('  run aliases.js');
        ns.tprint('\nQuick Start:');
        ns.tprint('  run auto-root.js         (Root all servers)');
        ns.tprint('  run find-target.js       (Find best target)');
        ns.tprint('  run smart-deploy.js      (Smart deploy - auto finds target!)');
        ns.tprint('  run buy-servers.js       (Buy/upgrade servers)');
        ns.tprint('  run faction-work.js "CyberSec" hacking');
        ns.tprint('\nAuto mode:');
        ns.tprint('  run auto-lite.js n00dles');
        ns.tprint('\nCheck files:');
        ns.tprint('  ls');
        
    } catch (error) {
        ns.tprint('\n!!! ERROR !!!');
        ns.tprint('Error during setup: ' + error);
        ns.tprint('Stack trace: ' + error.stack);
    }
}
