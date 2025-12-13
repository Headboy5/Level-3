/** @param {NS} ns */
// RAM Cost: ~3.5GB - Deploys hack script to all servers targeting specified server
export async function main(ns) {
    if (ns.args.length === 0) {
        ns.tprint('Usage: run deploy.js [target]');
        ns.tprint('Example: run deploy.js n00dles');
        return;
    }
    
    const target = ns.args[0];
    const servers = scanNetwork(ns);
    
    // Create hack/grow/weaken scripts
    const hackScript = `/** @param {NS} ns */
export async function main(ns) {
    const target = ns.args[0];
    while (true) {
        await ns.hack(target);
    }
}`;
    
    const growScript = `/** @param {NS} ns */
export async function main(ns) {
    const target = ns.args[0];
    while (true) {
        await ns.grow(target);
    }
}`;
    
    const weakenScript = `/** @param {NS} ns */
export async function main(ns) {
    const target = ns.args[0];
    while (true) {
        await ns.weaken(target);
    }
}`;
    
    await ns.write('/tmp/hack.js', hackScript, 'w');
    await ns.write('/tmp/grow.js', growScript, 'w');
    await ns.write('/tmp/weaken.js', weakenScript, 'w');
    
    // Get actual RAM costs for each script
    const hackRam = ns.getScriptRam('/tmp/hack.js');
    const growRam = ns.getScriptRam('/tmp/grow.js');
    const weakenRam = ns.getScriptRam('/tmp/weaken.js');
    
    let deployed = 0;
    for (const server of servers) {
        if (!ns.hasRootAccess(server)) continue;
        
        const maxRam = ns.getServerMaxRam(server);
        if (maxRam < 2) continue;
        
        // Copy scripts
        await ns.scp('/tmp/hack.js', server, 'home');
        await ns.scp('/tmp/grow.js', server, 'home');
        await ns.scp('/tmp/weaken.js', server, 'home');
        
        ns.killall(server);
        
        // Calculate available RAM
        const availableRam = maxRam - ns.getServerUsedRam(server);
        
        // Calculate max threads for each script type
        const maxWeakenThreads = Math.floor(availableRam / weakenRam);
        const maxGrowThreads = Math.floor(availableRam / growRam);
        const maxHackThreads = Math.floor(availableRam / hackRam);
        
        // Distribute threads: 50% weaken, 30% grow, 20% hack based on RAM
        const weakenThreads = Math.floor(maxWeakenThreads * 0.5);
        const growThreads = Math.floor(maxGrowThreads * 0.3);
        const hackThreads = Math.floor(maxHackThreads * 0.2);
        
        // Calculate actual RAM usage to maximize utilization
        let usedRam = (weakenThreads * weakenRam) + (growThreads * growRam) + (hackThreads * hackRam);
        let remainingRam = availableRam - usedRam;
        
        // Use remaining RAM for additional weaken threads (most important)
        const bonusWeakenThreads = Math.floor(remainingRam / weakenRam);
        const finalWeakenThreads = weakenThreads + bonusWeakenThreads;
        
        // Start scripts
        if (finalWeakenThreads > 0) {
            ns.exec('/tmp/weaken.js', server, finalWeakenThreads, target);
        }
        if (growThreads > 0) {
            ns.exec('/tmp/grow.js', server, growThreads, target);
        }
        if (hackThreads > 0) {
            ns.exec('/tmp/hack.js', server, hackThreads, target);
        }
        
        deployed++;
    }
    
    ns.tprint(`✓ Deployed to ${deployed} servers targeting ${target}`);
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
