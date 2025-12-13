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
        
        // Calculate threads for each script type
        const ramPerScript = 1.75; // Average RAM cost
        const totalThreads = Math.floor(maxRam / ramPerScript);
        
        // Distribute threads: 50% weaken, 30% grow, 20% hack
        const weakenThreads = Math.floor(totalThreads * 0.5);
        const growThreads = Math.floor(totalThreads * 0.3);
        const hackThreads = Math.floor(totalThreads * 0.2);
        
        // Start scripts
        if (weakenThreads > 0) {
            ns.exec('/tmp/weaken.js', server, weakenThreads, target);
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
