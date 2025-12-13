/** @param {NS} ns */
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
        ns.tprint(`Best target: ${bestTarget}`);
        ns.tprint(`  Max money: $${ns.formatNumber(ns.getServerMaxMoney(bestTarget))}`);
        ns.tprint(`  Required level: ${ns.getServerRequiredHackingLevel(bestTarget)}`);
        ns.tprint(`  Min security: ${ns.getServerMinSecurityLevel(bestTarget)}`);
        
        // Write target to port 1 for other scripts to read
        await ns.writePort(1, bestTarget);
        return bestTarget;
    } else {
        ns.tprint('No suitable targets found');
        await ns.writePort(1, null);
        return null;
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
