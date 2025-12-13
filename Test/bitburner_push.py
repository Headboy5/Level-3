"""
Bitburner File Pusher - Uses HTTP POST instead of WebSocket
Works when WebSocket connection fails
"""
import requests
import json
import os
from pathlib import Path
import time

BITBURNER_URL = "http://localhost:9990"  # Try different ports: 9990, 12525, 8080

def push_file(filename: str, content: str, server: str = "home") -> bool:
    """Push a single file to Bitburner via HTTP"""
    url = f"{BITBURNER_URL}/v1/pushFile"
    
    payload = {
        "filename": filename,
        "content": content,
        "server": server
    }
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            print(f"✓ {filename} ({len(content)} bytes)")
            return True
        else:
            print(f"✗ {filename}: {response.status_code} - {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print(f"✗ Connection failed - Is Bitburner running with API enabled?")
        print(f"   Trying to connect to: {BITBURNER_URL}")
        return False
    except Exception as e:
        print(f"✗ {filename}: {e}")
        return False

def sync_all_files(directory: str):
    """Push all .js files from directory"""
    script_dir = Path(directory)
    js_files = list(script_dir.glob("*.js"))
    
    if not js_files:
        print(f"\n⚠ No .js files found in {directory}")
        return
    
    print(f"\n=== Syncing {len(js_files)} files ===\n")
    
    success = 0
    for js_file in sorted(js_files):
        with open(js_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if push_file(js_file.name, content):
            success += 1
        time.sleep(0.1)  # Small delay between files
    
    print(f"\n=== {success}/{len(js_files)} files synced ===")

def watch_and_sync(directory: str):
    """Watch directory and sync on changes"""
    print("\n👀 Watching for file changes... (Ctrl+C to stop)")
    print(f"Directory: {directory}\n")
    
    last_modified = {}
    
    try:
        while True:
            script_dir = Path(directory)
            js_files = list(script_dir.glob("*.js"))
            
            for js_file in js_files:
                mtime = js_file.stat().st_mtime
                
                if js_file not in last_modified or last_modified[js_file] < mtime:
                    print(f"\n📝 Detected change: {js_file.name}")
                    
                    with open(js_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    push_file(js_file.name, content)
                    last_modified[js_file] = mtime
            
            time.sleep(1)  # Check every second
            
    except KeyboardInterrupt:
        print("\n\n✓ Stopped watching")

if __name__ == "__main__":
    import sys
    
    print("╔════════════════════════════════════════╗")
    print("║   Bitburner File Sync (HTTP Mode)     ║")
    print("╚════════════════════════════════════════╝")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    if len(sys.argv) > 1 and sys.argv[1] == "watch":
        # Initial sync
        sync_all_files(current_dir)
        # Then watch for changes
        watch_and_sync(current_dir)
    else:
        # One-time sync
        sync_all_files(current_dir)
        print("\nTip: Run 'python bitburner_push.py watch' to auto-sync on file changes")
