import sys
import subprocess
import shutil
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: KidsNetworkBuilder.exe <package_file> <video_file>")
        sys.exit(1)

    package_file = Path(sys.argv[1])
    video_file = Path(sys.argv[2])

    if not package_file.exists() or not video_file.exists():
        print("Error: Files not found.")
        sys.exit(1)

    # Placeholder: actual replacement logic should be implemented here
    print(f"Replacing video in {package_file} with {video_file}...")
    # TODO: Implement DBPF replacement

    # For now just copy the package as output
    output_file = package_file.parent / "Kids-Network-1.package"
    shutil.copy(package_file, output_file)
    print(f"Created {output_file}")

if __name__ == "__main__":
    main()
