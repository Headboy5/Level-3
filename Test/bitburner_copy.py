"""
Bitburner Direct File Copy
Copies .js files directly to game save directory
No API needed!
"""
import os
import shutil
from pathlib import Path

# Bitburner save locations
STEAM_SAVES = [
    Path.home() / "AppData/Roaming/bitburner",
    Path.home() / "Documents/Bitburner",
    "C:/Program Files (x86)/Steam/steamapps/common/Bitburner/resources/app/dist/ext",
]

BROWSER_SAVES = [
    Path.home() / "AppData/Local/bitburner-official/IndexedDB",
]

def find_bitburner_save():
    """Find Bitburner save directory"""
    print("🔍 Looking for Bitburner save directory...\n")
    
    for save_path in STEAM_SAVES + BROWSER_SAVES:
        if save_path.exists():
            print(f"✓ Found: {save_path}")
            return save_path
    
    print("✗ Could not auto-detect Bitburner save location")
    print("\nPlease find it manually:")
    print("  Steam: Usually C:/Users/[YOU]/AppData/Roaming/bitburner")
    print("  Browser: Check browser's Application > IndexedDB")
    return None

def copy_scripts(source_dir: str, dest_dir: Path):
    """Copy all .js files to Bitburner directory"""
    source = Path(source_dir)
    js_files = list(source.glob("*.js"))
    
    if not js_files:
        print(f"\n⚠ No .js files found in {source_dir}")
        return
    
    print(f"\n=== Copying {len(js_files)} files ===\n")
    
    # Create scripts subdirectory if needed
    scripts_dir = dest_dir / "scripts"
    scripts_dir.mkdir(exist_ok=True, parents=True)
    
    success = 0
    for js_file in sorted(js_files):
        try:
            dest_file = scripts_dir / js_file.name
            shutil.copy2(js_file, dest_file)
            print(f"✓ {js_file.name} → {dest_file}")
            success += 1
        except Exception as e:
            print(f"✗ {js_file.name}: {e}")
    
    print(f"\n=== {success}/{len(js_files)} files copied ===")
    print("\n⚠ IMPORTANT: Reload Bitburner (or load save) to see the files!")

if __name__ == "__main__":
    print("╔════════════════════════════════════════╗")
    print("║   Bitburner Direct File Copy          ║")
    print("╚════════════════════════════════════════╝\n")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = find_bitburner_save()
    
    if save_dir:
        copy_scripts(current_dir, save_dir)
    else:
        print("\n💡 Manual method:")
        print("1. Open Bitburner")
        print("2. In terminal: nano script.js")
        print("3. Paste your code")
        print("4. Ctrl+C to save")
        print("\nOr just copy-paste each file manually into the game terminal.")
