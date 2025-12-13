/** @param {NS} ns */
// RAM Cost: ~4.5GB - Intelligently deploys scripts with calculated thread ratios
export async function main(ns) {
    // Auto-find target if not specified
    let target = ns.args[0];
    if (!target) {
        ns.tprint('No target specified, finding best target...');
        ns.run('find-target.js');
        await ns.sleep(2000); // Wait for find-target to complete
        
        // Read target from port 1
        target = ns.readPort(1);
        if (target === 'NULL PORT DATA' || !target) {
            // Fallback: manually find a target
            const servers = scanNetwork(ns);
            for (const server of servers) {
                if (ns.hasRootAccess(server) && ns.getServerMaxMoney(server) > 0) {
                    target = server;
                    break;
                }
            }
        }
        
        if (!target) {
            ns.tprint('ERROR: No suitable target found!');
            return;
        }
        ns.tprint('Auto-selected target: ' + target);
    }
    
    const servers = scanNetwork(ns);
    
    // Create optimized scripts
    const hackScript = '/** @param {NS} ns */\nexport async function main(ns) {\n    const target = ns.args[0];\n    while (true) {\n        await ns.hack(target);\n    }\n}';
    
    const growScript = '/** @param {NS} ns */\nexport async function main(ns) {\n    const target = ns.args[0];\n    while (true) {\n        await ns.grow(target);\n    }\n}';
    
    const weakenScript = '/** @param {NS} ns */\nexport async function main(ns) {\n    const target = ns.args[0];\n    while (true) {\n        await ns.weaken(target);\n    }\n}';
    
    await ns.write('/tmp/hack.js', hackScript, 'w');
    await ns.write('/tmp/grow.js', growScript, 'w');
    await ns.write('/tmp/weaken.js', weakenScript, 'w');
    
    // Get RAM costs
    const hackRam = ns.getScriptRam('/tmp/hack.js');
    const growRam = ns.getScriptRam('/tmp/grow.js');
    const weakenRam = ns.getScriptRam('/tmp/weaken.js');
    
    // Analyze target server state
    const currentSecurity = ns.getServerSecurityLevel(target);
    const minSecurity = ns.getServerMinSecurityLevel(target);
    const currentMoney = ns.getServerMoneyAvailable(target);
    const maxMoney = ns.getServerMaxMoney(target);
    
    const securityDiff = currentSecurity - minSecurity;
    const moneyPercent = maxMoney > 0 ? currentMoney / maxMoney : 0;
    
    ns.tprint('=== Target Analysis ===');
    ns.tprint('Server: ' + target);
    ns.tprint('Security: ' + currentSecurity.toFixed(2) + ' / ' + minSecurity.toFixed(2) + ' (diff: ' + securityDiff.toFixed(2) + ')');
    ns.tprint('Money: $' + ns.formatNumber(currentMoney) + ' / $' + ns.formatNumber(maxMoney) + ' (' + (moneyPercent * 100).toFixed(1) + '%)');
    
    // Calculate thread ratios based on server state
    let weakenRatio, growRatio, hackRatio;
    
    if (securityDiff > 5) {
        // High security: focus on weakening
        weakenRatio = 0.70;
        growRatio = 0.25;
        hackRatio = 0.05;
        ns.tprint('Strategy: WEAKEN-HEAVY (high security)');
    } else if (moneyPercent < 0.5) {
        // Low money: focus on growing
        weakenRatio = 0.40;
        growRatio = 0.50;
        hackRatio = 0.10;
        ns.tprint('Strategy: GROW-HEAVY (low money)');
    } else if (moneyPercent < 0.75) {
        // Medium money: balanced grow
        weakenRatio = 0.45;
        growRatio = 0.40;
        hackRatio = 0.15;
        ns.tprint('Strategy: BALANCED-GROW');
    } else {
        // Good state: normal operation
        weakenRatio = 0.50;
        growRatio = 0.30;
        hackRatio = 0.20;
        ns.tprint('Strategy: NORMAL OPERATION');
    }
    
    let deployed = 0;
    let totalWeaken = 0, totalGrow = 0, totalHack = 0;
    
    for (const server of servers) {
        if (!ns.hasRootAccess(server)) continue;
        
        const maxRam = ns.getServerMaxRam(server);
        if (maxRam < 2) continue;
        
        // Copy scripts
        await ns.scp('/tmp/hack.js', server, 'home');
        await ns.scp('/tmp/grow.js', server, 'home');
        await ns.scp('/tmp/weaken.js', server, 'home');
        
        ns.killall(server);
        
        // Calculate available RAM (reserve some on home)
        let availableRam = maxRam - ns.getServerUsedRam(server);
        if (server === 'home') {
            availableRam = Math.max(0, availableRam - 50); // Reserve 50GB on home
        }
        
        if (availableRam < Math.min(hackRam, growRam, weakenRam)) continue;
        
        // Calculate threads based on ratios
        const totalPossibleThreads = Math.floor(availableRam / ((weakenRatio * weakenRam) + (growRatio * growRam) + (hackRatio * hackRam)));
        
        const weakenThreads = Math.max(1, Math.floor(totalPossibleThreads * weakenRatio));
        const growThreads = Math.max(1, Math.floor(totalPossibleThreads * growRatio));
        const hackThreads = Math.max(1, Math.floor(totalPossibleThreads * hackRatio));
        
        // Verify we have enough RAM
        const neededRam = (weakenThreads * weakenRam) + (growThreads * growRam) + (hackThreads * hackRam);
        if (neededRam > availableRam) {
            // Scale down proportionally
            const scale = availableRam / neededRam;
            const adjustedWeaken = Math.floor(weakenThreads * scale);
            const adjustedGrow = Math.floor(growThreads * scale);
            const adjustedHack = Math.floor(hackThreads * scale);
            
            if (adjustedWeaken > 0) ns.exec('/tmp/weaken.js', server, adjustedWeaken, target);
            if (adjustedGrow > 0) ns.exec('/tmp/grow.js', server, adjustedGrow, target);
            if (adjustedHack > 0) ns.exec('/tmp/hack.js', server, adjustedHack, target);
            
            totalWeaken += adjustedWeaken;
            totalGrow += adjustedGrow;
            totalHack += adjustedHack;
        } else {
            // Execute with calculated threads
            if (weakenThreads > 0) ns.exec('/tmp/weaken.js', server, weakenThreads, target);
            if (growThreads > 0) ns.exec('/tmp/grow.js', server, growThreads, target);
            if (hackThreads > 0) ns.exec('/tmp/hack.js', server, hackThreads, target);
            
            totalWeaken += weakenThreads;
            totalGrow += growThreads;
            totalHack += hackThreads;
        }
        
        deployed++;
    }
    
    ns.tprint('\n=== Deployment Summary ===');
    ns.tprint('Deployed to ' + deployed + ' servers');
    ns.tprint('Total threads: Weaken=' + totalWeaken + ', Grow=' + totalGrow + ', Hack=' + totalHack);
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
