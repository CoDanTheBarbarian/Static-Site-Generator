import os
import shutil

from copystatic import recursive_file_copy

dir_path_static = "/root/workspace/github.com/CoDanTheBarbarian/static_site_generator/static"
dir_path_public = "/root/workspace/github.com/CoDanTheBarbarian/static_site_generator/public"

def main():
    print("Deleting public files...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory...")
    recursive_file_copy(dir_path_static, dir_path_public)


if __name__ == "__main__":
    main()