import sys
import shutil
import os

def replace_video(package_path, video_path):
    # Create output path
    base, ext = os.path.splitext(package_path)
    output_path = f"{base}_updated{ext}"

    # For now: just simulate replacing video
    # (In reality you'd inject the video into the correct STBL or binary stream)
    shutil.copy(package_path, output_path)

    print(f"✅ Created new package: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python KidsNetworkBuilder.py <package_file> <video_file>")
        sys.exit(1)

    package_file = sys.argv[1]
    video_file = sys.argv[2]

    replace_video(package_file, video_file)
