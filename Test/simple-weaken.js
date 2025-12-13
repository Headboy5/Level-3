/** @param {NS} ns */
// RAM Cost: ~1.75GB - Simple weaken script
export async function main(ns) {
    const target = ns.args[0] || 'n00dles';
    
    while (true) {
        await ns.weaken(target);
    }
}
