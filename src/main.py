import os
import shutil

from copystatic import recursive_file_copy
from generate_page import generate_page

dir_path_static = "/root/workspace/github.com/CoDanTheBarbarian/static_site_generator/static"
dir_path_public = "/root/workspace/github.com/CoDanTheBarbarian/static_site_generator/public"
dir_path_content = "/root/workspace/github.com/CoDanTheBarbarian/static_site_generator/content"
template_path = "/root/workspace/github.com/CoDanTheBarbarian/static_site_generator/template.html"

def main():
    print("Deleting public files...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory...")
    recursive_file_copy(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"), 
        template_path, 
        os.path.join(dir_path_public, "index.html")
        )



if __name__ == "__main__":
    main()