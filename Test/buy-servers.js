/** @param {NS} ns */
// RAM Cost: ~5.0GB - Automatically purchases and upgrades servers
export async function main(ns) {
    ns.disableLog('ALL');
    const maxServers = ns.getPurchasedServerLimit();
    const currentServers = ns.getPurchasedServers();
    
    ns.tprint('=== Server Purchase Manager ===');
    ns.tprint('Current servers: ' + currentServers.length + ' / ' + maxServers);
    ns.tprint('Available money: $' + ns.formatNumber(ns.getServerMoneyAvailable('home')));
    
    // Define RAM tiers (must be powers of 2)
    const ramTiers = [8, 16, 32, 64, 128, 256, 512, 1024];
    
    // Buy new servers if under limit
    if (currentServers.length < maxServers) {
        ns.tprint('\n--- Buying New Servers ---');
        
        for (let i = currentServers.length; i < maxServers; i++) {
            // Find highest affordable RAM tier
            let buyRam = 8;
            for (const ram of ramTiers) {
                const cost = ns.getPurchasedServerCost(ram);
                if (ns.getServerMoneyAvailable('home') >= cost * 1.5) { // Keep some reserve
                    buyRam = ram;
                } else {
                    break;
                }
            }
            
            const cost = ns.getPurchasedServerCost(buyRam);
            const money = ns.getServerMoneyAvailable('home');
            
            if (money >= cost * 1.5) {
                const hostname = ns.purchaseServer('pserv-' + i, buyRam);
                if (hostname) {
                    ns.tprint('✓ Purchased: ' + hostname + ' with ' + buyRam + 'GB RAM ($' + ns.formatNumber(cost) + ')');
                } else {
                    ns.tprint('✗ Failed to purchase server');
                    break;
                }
            } else {
                ns.tprint('Not enough money for more servers (need $' + ns.formatNumber(cost * 1.5) + ')');
                break;
            }
        }
    }
    
    // Upgrade existing servers
    ns.tprint('\n--- Checking Upgrades ---');
    for (const server of currentServers) {
        const currentRam = ns.getServerMaxRam(server);
        
        // Find next RAM tier
        let nextRam = null;
        for (const ram of ramTiers) {
            if (ram > currentRam) {
                nextRam = ram;
                break;
            }
        }
        
        if (!nextRam) {
            ns.tprint('✓ ' + server + ' already at max (' + currentRam + 'GB)');
            continue;
        }
        
        const upgradeCost = ns.getPurchasedServerCost(nextRam);
        const money = ns.getServerMoneyAvailable('home');
        
        if (money >= upgradeCost * 2) { // Keep larger reserve for upgrades
            // Delete old server and buy new one with same name
            const serverId = server.split('-')[1];
            ns.killall(server);
            ns.deleteServer(server);
            
            const hostname = ns.purchaseServer('pserv-' + serverId, nextRam);
            if (hostname) {
                ns.tprint('✓ Upgraded ' + server + ': ' + currentRam + 'GB → ' + nextRam + 'GB ($' + ns.formatNumber(upgradeCost) + ')');
            } else {
                ns.tprint('✗ Failed to upgrade ' + server);
            }
        } else {
            ns.tprint('• ' + server + ': ' + currentRam + 'GB (upgrade to ' + nextRam + 'GB costs $' + ns.formatNumber(upgradeCost) + ')');
        }
    }
    
    ns.tprint('\n=== Summary ===');
    const updatedServers = ns.getPurchasedServers();
    let totalRam = 0;
    for (const server of updatedServers) {
        totalRam += ns.getServerMaxRam(server);
    }
    ns.tprint('Total servers: ' + updatedServers.length);
    ns.tprint('Total RAM: ' + totalRam + 'GB');
    ns.tprint('Remaining money: $' + ns.formatNumber(ns.getServerMoneyAvailable('home')));
    
    // Auto-deploy if requested
    if (ns.args[0] === 'deploy' && ns.args[1]) {
        ns.tprint('\n--- Auto-deploying to ' + ns.args[1] + ' ---');
        await ns.sleep(1000);
        ns.run('smart-deploy.js', 1, ns.args[1]);
    }
}
