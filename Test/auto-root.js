/** @param {NS} ns */
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
                ns.tprint(`✓ Rooted ${server}`);
            } catch (e) {}
        }
    }
    
    ns.tprint(`Total: ${servers.length} servers, ${newRoots} newly rooted`);
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
