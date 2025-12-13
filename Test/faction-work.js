/** @param {NS} ns */
// RAM Cost: ~2.0GB - Does faction work with unused home RAM
export async function main(ns) {
    ns.disableLog('ALL');
    
    // Get current faction (you'll need to set this)
    const faction = ns.args[0];
    if (!faction) {
        ns.tprint('Usage: run faction-work.js [faction-name] [work-type]');
        ns.tprint('Work types: hacking, field, security');
        ns.tprint('Example: run faction-work.js "CyberSec" hacking');
        return;
    }
    
    const workType = ns.args[1] || 'hacking';
    
    ns.tprint('=== Faction Work Manager ===');
    ns.tprint('Faction: ' + faction);
    ns.tprint('Work type: ' + workType);
    
    // Calculate how much RAM is free on home
    const homeMaxRam = ns.getServerMaxRam('home');
    const homeUsedRam = ns.getServerUsedRam('home');
    const homeFreeRam = homeMaxRam - homeUsedRam;
    
    ns.tprint('Home RAM: ' + homeUsedRam.toFixed(2) + 'GB / ' + homeMaxRam + 'GB');
    ns.tprint('Free RAM: ' + homeFreeRam.toFixed(2) + 'GB');
    
    // If we have at least 50GB free, suggest dedicating it to hacking instead
    if (homeFreeRam >= 50) {
        ns.tprint('\n⚠ You have ' + homeFreeRam.toFixed(0) + 'GB free on home!');
        ns.tprint('Consider running: run smart-deploy.js');
        ns.tprint('This will use that RAM for hacking scripts.');
    }
    
    // Start faction work
    ns.tprint('\nStarting faction work...');
    
    try {
        if (workType === 'hacking') {
            const success = ns.singularity.workForFaction(faction, 'hacking', false);
            if (success) {
                ns.tprint('✓ Started hacking work for ' + faction);
            } else {
                ns.tprint('✗ Failed to start faction work (do you have Singularity API access?)');
            }
        } else if (workType === 'field') {
            const success = ns.singularity.workForFaction(faction, 'field', false);
            if (success) {
                ns.tprint('✓ Started field work for ' + faction);
            } else {
                ns.tprint('✗ Failed to start faction work');
            }
        } else if (workType === 'security') {
            const success = ns.singularity.workForFaction(faction, 'security', false);
            if (success) {
                ns.tprint('✓ Started security work for ' + faction);
            } else {
                ns.tprint('✗ Failed to start faction work');
            }
        }
    } catch (e) {
        ns.tprint('✗ ERROR: ' + e);
        ns.tprint('\nNote: Faction work requires Singularity API (Source-File 4)');
        ns.tprint('If you don\'t have it yet, faction work must be done manually.');
    }
    
    ns.tprint('\n=== Tip ===');
    ns.tprint('Run smart-deploy.js to automatically use free RAM for money-making!');
}
