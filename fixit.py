import os
import subprocess

def system_call(args, cwd="."):
    print("Running '{}' in '{}'".format(' '.join(args), cwd))
    subprocess.run(args, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def fix_image_files(root=os.curdir):
    convert_path = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\convert.exe"
    assets_dir = os.path.join(root, "assets")
    for path, dirs, files in os.walk(assets_dir):
        for file in files:
            if file.endswith(".png"):
                file_path = os.path.join(path, file)
                system_call([convert_path, file_path, "-strip", file_path])

try:
    fix_image_files()
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")
