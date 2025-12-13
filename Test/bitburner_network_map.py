"""
Bitburner Network Map Generator for Trillium
Reads network data from a JSON file exported from Bitburner and creates
hierarchical notes in Trillium using trilium-py.
"""

from trilium_py.client import ETAPI
import json

# ===== CONFIGURATION =====
TRILIUM_URL = 'https://notes.hexwood.zip'
ETAPI_TOKEN = 'RJb25V7DvBLP_Hvkr5fgWD1j+Ygy2B6QW7Wd7DsFYol6oPlhw4mNuJGo='
PARENT_NOTE_ID = 'Pp2tV8HHCBMo'    # Where to create the network map

# Check if configured
if ETAPI_TOKEN == 'YOUR_TOKEN_HERE':
    print('ERROR: Please configure TRILIUM_URL and ETAPI_TOKEN!')
    print('Get your ETAPI token from Trillium: Options -> ETAPI')
    exit(1)

# Initialize ETAPI client
ea = ETAPI(TRILIUM_URL, ETAPI_TOKEN)

# Test connection
try:
    app_info = ea.app_info()
    print(f"Connected to Trilium {app_info['appVersion']}")
except Exception as e:
    print(f"ERROR: Failed to connect to Trillium: {e}")
    exit(1)


def create_server_note(server_data, parent_note_id):
    """
    Create a note for a server with detailed information.
    
    Args:
        server_data: Dictionary containing server information
        parent_note_id: Parent note ID to create this note under
        
    Returns:
        The created note ID
    """
    hostname = server_data['hostname']
    has_root = server_data.get("hasRoot", False)
    req_hack_level = server_data.get("requiredHackingLevel", 0)
    num_ports = server_data.get("numPortsRequired", 0)
    max_ram = server_data.get("maxRam", 0)
    max_money = server_data.get('maxMoney', 0)
    money = server_data.get('money', 0)
    growth = server_data.get("growth", 0)
    security = server_data.get('security', 0)
    min_security = server_data.get('minSecurity', 0)
    
    # Build HTML content with server details
    content = '<h3>Server Information</h3>'
    content += '<ul>'
    content += f'<li><strong>Hostname:</strong> {hostname}</li>'
    content += f'<li><strong>Root Access:</strong> {"✓ Yes" if has_root else "✗ No"}</li>'
    content += f'<li><strong>Required Hacking Level:</strong> {req_hack_level}</li>'
    content += f'<li><strong>Ports Required:</strong> {num_ports}</li>'
    content += f'<li><strong>RAM:</strong> {max_ram} GB</li>'
    
    if max_money > 0:
        content += f'<li><strong>Money:</strong> ${money:,.2f} / ${max_money:,.2f}</li>'
        content += f'<li><strong>Growth:</strong> {growth}</li>'
    
    content += f'<li><strong>Security:</strong> {security:.2f} (min: {min_security:.2f})</li>'
    content += '</ul>'
    
    # Create note title
    title = f"🏠 {hostname}" if hostname == 'home' else hostname
    
    print(f"Creating note: {title}")
    
    # Create the note
    result = ea.create_note(
        parentNoteId=parent_note_id,
        title=title,
        type='text',
        content=content
    )
    
    note_id = result['note']['noteId']
    
    # Create labels for easy searching
    ea.create_attribute(noteId=note_id, type='label', name='server', value=hostname, isInheritable=False)
    ea.create_attribute(noteId=note_id, type='label', name='rootAccess', value='true' if has_root else 'false', isInheritable=False)
    ea.create_attribute(noteId=note_id, type='label', name='hackLevel', value=str(req_hack_level), isInheritable=False)
    ea.create_attribute(noteId=note_id, type='label', name='portsRequired', value=str(num_ports), isInheritable=False)
    ea.create_attribute(noteId=note_id, type='label', name='ram', value=str(max_ram), isInheritable=False)
    
    if max_money > 0:
        ea.create_attribute(noteId=note_id, type='label', name='maxMoney', value=str(int(max_money)), isInheritable=False)
        ea.create_attribute(noteId=note_id, type='label', name='growth', value=str(growth), isInheritable=False)
    
    ea.create_attribute(noteId=note_id, type='label', name='security', value=f"{security:.2f}", isInheritable=False)
    ea.create_attribute(noteId=note_id, type='label', name='minSecurity', value=f"{min_security:.2f}", isInheritable=False)
    
    return note_id


def create_network_tree(network_data, parent_note_id, visited=None):
    """
    Recursively create notes for the network tree.
    
    Args:
        network_data: Dictionary with server data and connections
        parent_note_id: Parent note ID to create notes under
        visited: Set of already visited servers (to prevent loops)
    """
    if visited is None:
        visited = set()
    
    hostname = network_data['hostname']
    
    # Skip if already visited
    if hostname in visited:
        return
    
    visited.add(hostname)
    
    # Create note for this server
    note_id = create_server_note(network_data, parent_note_id)
    
    # Process connected servers
    connections = network_data.get('connections', [])
    for connection in connections:
        create_network_tree(connection, note_id, visited)


def main():
    """Main function to create the network map in Trillium."""
    
    # Load network data from JSON file
    # You'll need to export this from Bitburner
    try:
        with open('network_data.json', 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                print("ERROR: network_data.json is empty!")
                print("\nPlease follow these steps:")
                print("1. Run this script in Bitburner: run export_network.js")
                print("2. Open the network_data.txt file in Bitburner")
                print("3. Copy ALL the JSON content")
                print("4. Save it as network_data.json in this folder")
                print(f"\nCurrent folder: {__file__.rsplit('/', 1)[0] if '/' in __file__ else __file__.rsplit(chr(92), 1)[0]}")
                return
            network_data = json.loads(content)
    except FileNotFoundError:
        print("ERROR: network_data.json not found!")
        print("\nPlease create this file by running the following script in Bitburner:")
        print("\n" + "="*60)
        print(BITBURNER_EXPORT_SCRIPT)
        print("="*60)
        print("\nThen copy the content from network_data.txt and save as network_data.json")
        return
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in network_data.json: {e}")
        print("\nMake sure you copied the COMPLETE JSON content from Bitburner's network_data.txt")
        print("The file should start with { and end with }")
        return
    
    print('Creating Bitburner Network Map in Trillium...')
    
    # Create main network map note
    main_note = ea.create_note(
        parentNoteId=PARENT_NOTE_ID,
        title='🌐 Bitburner Network Map',
        type='text',
        content='<p>Network map generated from Bitburner</p>'
    )
    
    main_note_id = main_note['note']['noteId']
    print(f"Created main note: {main_note_id}")
    
    # Create the network tree
    create_network_tree(network_data, main_note_id)
    
    print('\n✓ Network map created successfully in Trillium!')
    print('Open Trillium and navigate to the "🌐 Bitburner Network Map" note.')


# Bitburner script to export network data
BITBURNER_EXPORT_SCRIPT = '''/** @param {NS} ns */
export async function main(ns) {
    const visited = new Set();
    
    function scanNetwork(server) {
        if (visited.has(server)) return null;
        visited.add(server);
        
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
    
    const networkData = scanNetwork('home');
    
    // Save to file
    ns.write('network_data.txt', JSON.stringify(networkData, null, 2), 'w');
    ns.tprint('Network data exported to network_data.txt');
    ns.tprint('Copy this file content and save as network_data.json in your Python script folder');
}'''


if __name__ == '__main__':
    main()
