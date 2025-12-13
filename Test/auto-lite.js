/** @param {NS} ns */
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
        ns.tprint(`--- Deploying scripts to target: ${target} ---`);
        await ns.run('deploy.js', 1, target);
        await ns.sleep(5000);
        
        // Wait before next cycle
        ns.tprint('Waiting 5 minutes before next cycle...');
        await ns.sleep(300000); // 5 minutes
    }
}
