import os
import shutil

def recursive_file_copy(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for file_name in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, file_name)
        dest_path = os.path.join(dest_dir_path, file_name)
        print(f"{from_path} copying to: {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            recursive_file_copy(from_path, dest_path)