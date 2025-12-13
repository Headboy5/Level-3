"""
Bitburner Remote API Sync Tool
Pushes all .js files to Bitburner via websocket connection
"""
import asyncio
import websockets
import json
import os
from pathlib import Path

# Configuration
# Change this port to match what you set in Bitburner Options > Remote API > Port
BITBURNER_PORT = 12525  # Common ports: 9990, 12525, 8080
BITBURNER_HOST = "localhost"  # Or try "127.0.0.1"
BITBURNER_WS_URL = f"ws://{BITBURNER_HOST}:{BITBURNER_PORT}"
SERVER_NAME = "home"  # Target server in Bitburner

class BitburnerSync:
    def __init__(self, ws_url: str, server: str):
        self.ws_url = ws_url
        self.server = server
        self.ws = None
        self.request_id = 1
    
    async def connect(self):
        """Connect to Bitburner websocket"""
        print(f"Attempting to connect to {self.ws_url}...")
        
        try:
            # Try connecting with a timeout
            self.ws = await asyncio.wait_for(
                websockets.connect(
                    self.ws_url,
                    ping_interval=None,
                    close_timeout=10
                ),
                timeout=5
            )
            print(f"✓ Connected to Bitburner at {self.ws_url}")
            return True
        except asyncio.TimeoutError:
            print(f"✗ Connection timeout")
            self._print_troubleshooting()
            return False
        except ConnectionRefusedError:
            print(f"✗ Connection refused - server not listening on port {BITBURNER_PORT}")
            self._print_troubleshooting()
            return False
        except Exception as e:
            print(f"✗ Failed to connect: {type(e).__name__}: {e}")
            self._print_troubleshooting()
            return False
    
    def _print_troubleshooting(self):
        """Print troubleshooting steps"""
        print("\n⚠ CONNECTION FAILED - Troubleshooting:")
        print("\n1. In Bitburner game:")
        print("   - Go to: Options > Remote API")
        print(f"   - Set Port to: {BITBURNER_PORT}")
        print("   - Hostname should be: localhost")
        print("   - Click 'Connect' button")
        print("   - Wait for Status to show 'Online' (green)")
        print("\n2. Check if Bitburner is running in browser")
        print("\n3. Try these alternative ports in Bitburner settings:")
        print("   - 9990")
        print("   - 8080")
        print("   - 12525 (current)")
        print(f"\n4. If using different port, update line 11 in this script:")
        print(f"   BITBURNER_PORT = {BITBURNER_PORT}")
        print("\n5. Check Windows Firewall isn't blocking the connection")
        print("\n6. Try running Bitburner in Steam if you're using browser (or vice versa)")
    
    async def disconnect(self):
        """Disconnect from Bitburner"""
        if self.ws:
            await self.ws.close()
    
    async def push_file(self, filename: str, content: str) -> bool:
        """Push a file to Bitburner"""
        request = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": "pushFile",
            "params": {
                "filename": filename,
                "content": content,
                "server": self.server
            }
        }
        self.request_id += 1
        
        try:
            await self.ws.send(json.dumps(request))
            response = await self.ws.recv()
            result = json.loads(response)
            
            if "error" in result:
                print(f"✗ Error pushing {filename}: {result['error']}")
                return False
            else:
                print(f"✓ Pushed {filename} ({len(content)} bytes)")
                return True
        except Exception as e:
            print(f"✗ Failed to push {filename}: {e}")
            return False
    
    async def get_file(self, filename: str) -> str:
        """Get a file from Bitburner"""
        request = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": "getFile",
            "params": {
                "filename": filename,
                "server": self.server
            }
        }
        self.request_id += 1
        
        try:
            await self.ws.send(json.dumps(request))
            response = await self.ws.recv()
            result = json.loads(response)
            
            if "error" in result:
                return None
            else:
                return result.get("result", "")
        except Exception as e:
            print(f"✗ Failed to get {filename}: {e}")
            return None
    
    async def get_all_files(self) -> list:
        """Get all files from Bitburner server"""
        request = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": "getAllFiles",
            "params": {
                "server": self.server
            }
        }
        self.request_id += 1
        
        try:
            await self.ws.send(json.dumps(request))
            response = await self.ws.recv()
            result = json.loads(response)
            
            if "error" in result:
                print(f"✗ Error getting files: {result['error']}")
                return []
            else:
                return result.get("result", [])
        except Exception as e:
            print(f"✗ Failed to get files: {e}")
            return []
    
    async def calculate_ram(self, filename: str) -> float:
        """Calculate RAM cost of a script"""
        request = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": "calculateRam",
            "params": {
                "filename": filename,
                "server": self.server
            }
        }
        self.request_id += 1
        
        try:
            await self.ws.send(json.dumps(request))
            response = await self.ws.recv()
            result = json.loads(response)
            
            if "error" in result:
                return -1
            else:
                return result.get("result", -1)
        except Exception as e:
            print(f"✗ Failed to calculate RAM: {e}")
            return -1


async def sync_directory(directory: str, server: str = "home"):
    """Sync all .js files from directory to Bitburner"""
    sync = BitburnerSync(BITBURNER_WS_URL, server)
    
    if not await sync.connect():
        return
    
    try:
        # Find all .js files in directory
        script_dir = Path(directory)
        js_files = list(script_dir.glob("*.js"))
        
        if not js_files:
            print(f"\n⚠ No .js files found in {directory}")
            return
        
        print(f"\n=== Syncing {len(js_files)} files to Bitburner ===\n")
        
        success_count = 0
        for js_file in js_files:
            with open(js_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if await sync.push_file(js_file.name, content):
                success_count += 1
                
                # Calculate and display RAM cost
                ram = await sync.calculate_ram(js_file.name)
                if ram >= 0:
                    print(f"  RAM cost: {ram:.2f}GB")
        
        print(f"\n=== Summary ===")
        print(f"✓ Successfully pushed {success_count}/{len(js_files)} files")
        
    finally:
        await sync.disconnect()


async def pull_from_bitburner(server: str = "home"):
    """Pull all files from Bitburner to local directory"""
    sync = BitburnerSync(BITBURNER_WS_URL, server)
    
    if not await sync.connect():
        return
    
    try:
        print(f"\n=== Pulling files from Bitburner ===\n")
        files = await sync.get_all_files()
        
        if not files:
            print("⚠ No files found or error occurred")
            return
        
        output_dir = Path("./bitburner_files")
        output_dir.mkdir(exist_ok=True)
        
        for file_info in files:
            filename = file_info.get("filename", "")
            content = file_info.get("content", "")
            
            if filename:
                output_path = output_dir / filename
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Pulled {filename} ({len(content)} bytes)")
        
        print(f"\n✓ Pulled {len(files)} files to {output_dir}")
        
    finally:
        await sync.disconnect()


async def main():
    print("╔════════════════════════════════════════╗")
    print("║   Bitburner Remote API Sync Tool      ║")
    print("╚════════════════════════════════════════╝\n")
    
    print(f"Configuration:")
    print(f"  Host: {BITBURNER_HOST}")
    print(f"  Port: {BITBURNER_PORT}")
    print(f"  URL:  {BITBURNER_WS_URL}")
    print(f"  Server: {SERVER_NAME}\n")
    
    print("Options:")
    print("  1. Push all .js files to Bitburner")
    print("  2. Pull all files from Bitburner")
    print("  3. Test connection only")
    print("  4. Exit")
    
    choice = input("\nSelect option (1-4): ").strip()
    
    if choice == "1":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"\nPushing files from: {current_dir}")
        await sync_directory(current_dir)
    elif choice == "2":
        await pull_from_bitburner()
    elif choice == "3":
        print("\nTesting connection...")
        sync = BitburnerSync(BITBURNER_WS_URL, SERVER_NAME)
        if await sync.connect():
            print("✓ Connection successful!")
            await sync.disconnect()
        else:
            print("✗ Connection failed - see troubleshooting above")
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid option")


if __name__ == "__main__":
    asyncio.run(main())
