/** @param {NS} ns */
export async function main(ns) {
    const visited = new Set();
    
    // Recursively scan the network and build a tree structure
    function scanNetwork(server) {
        if (visited.has(server)) return null;
        visited.add(server);
        
        // Collect server information
        const serverData = {
            hostname: server,
            hasRoot: ns.hasRootAccess(server),
            money: ns.getServerMoneyAvailable(server),
            maxMoney: ns.getServerMaxMoney(server),
            security: ns.getServerSecurityLevel(server),
            minSecurity: ns.getServerMinSecurityLevel(server),
            requiredHackingLevel: ns.getServerRequiredHackingLevel(server),
            numPortsRequired: ns.getServerNumPortsRequired(server),
            maxRam: ns.getServerMaxRam(server),
            growth: ns.getServerGrowth(server),
            connections: []
        };
        
        // Get all connected servers
        const connections = ns.scan(server);
        for (const connected of connections) {
            if (!visited.has(connected)) {
                const connectedData = scanNetwork(connected);
                if (connectedData) {
                    serverData.connections.push(connectedData);
                }
            }
        }
        
        return serverData;
    }
    
    ns.tprint('Scanning network...');
    const networkData = scanNetwork('home');
    
    // Convert to JSON and save
    const jsonData = JSON.stringify(networkData, null, 2);
    ns.write('network_data.txt', jsonData, 'w');
    
    ns.tprint('\n✓ Network data exported to network_data.txt');
    ns.tprint(`Total servers scanned: ${visited.size}`);
    ns.tprint('\nNext steps:');
    ns.tprint('1. Copy the content of network_data.txt');
    ns.tprint('2. Save it as network_data.json in your Python script folder');
    ns.tprint('3. Run the Python script: python bitburner_network_map.py');
}
