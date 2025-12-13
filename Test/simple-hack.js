/** @param {NS} ns */
// RAM Cost: ~1.7GB - Simple hack script
export async function main(ns) {
    const target = ns.args[0] || 'n00dles';
    
    while (true) {
        await ns.hack(target);
    }
}
