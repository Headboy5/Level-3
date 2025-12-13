/** @param {NS} ns */
// Setup script - Creates all necessary automation files
export async function main(ns) {
    ns.tprint('==========================================');
    ns.tprint('Starting setup...');
    ns.tprint('==========================================');
    ns.disableLog('ALL');
    
    try {
        // Create auto-root script
        ns.tprint('\n[1/7] Creating auto-root.js...');
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
        ns.tprint('[2/7] Creating find-target.js...');
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
    } else {
        ns.tprint('No suitable targets found');
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
        ns.tprint('[3/7] Creating deploy.js...');
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
        
        // Create simple hack script
        ns.tprint('[4/7] Creating simple-hack.js...');
        const simpleHackScript = `/** @param {NS} ns */
// RAM Cost: ~1.7GB - Simple hack script
export async function main(ns) {
    const target = ns.args[0] || 'n00dles';
    
    while (true) {
        await ns.hack(target);
    }
}`;
        
        // Create simple grow script
        ns.tprint('[5/7] Creating simple-grow.js...');
        const simpleGrowScript = `/** @param {NS} ns */
// RAM Cost: ~1.75GB - Simple grow script
export async function main(ns) {
    const target = ns.args[0] || 'n00dles';
    
    while (true) {
        await ns.grow(target);
    }
}`;
        
        // Create simple weaken script
        ns.tprint('[6/7] Creating simple-weaken.js...');
        const simpleWeakenScript = `/** @param {NS} ns */
// RAM Cost: ~1.75GB - Simple weaken script
export async function main(ns) {
    const target = ns.args[0] || 'n00dles';
    
    while (true) {
        await ns.weaken(target);
    }
}`;
        
        // Create auto-lite script
        ns.tprint('[7/7] Creating auto-lite.js...');
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
        
        ns.tprint('\n===========================================');
        ns.tprint('✓ SUCCESS! All scripts created!');
        ns.tprint('===========================================');
        ns.tprint('\nQuick Start (choose one):');
        ns.tprint('  Individual commands:');
        ns.tprint('    run auto-root.js     (Root all servers)');
        ns.tprint('    run find-target.js   (Find best target)');
        ns.tprint('    run deploy.js n00dles (Deploy to target)');
        ns.tprint('\n  Or run everything automatically:');
        ns.tprint('    run auto-lite.js n00dles');
        ns.tprint('\n  Check files created:');
        ns.tprint('    ls');
        
    } catch (error) {
        ns.tprint('\n!!! ERROR !!!');
        ns.tprint('Error during setup: ' + error);
        ns.tprint('Stack trace: ' + error.stack);
    }
}
