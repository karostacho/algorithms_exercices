import os

def list_directory(path_to_search):
    rootdir = os.listdir(path_to_search)
    for item in rootdir:
        dir = os.path.join(path_to_search, item)
        if os.path.isdir(dir):
            print(f"folder: {os.path.basename(dir)}")
            list_directory(dir)
        if os.path.isfile(dir):
            print(f"file: {os.path.basename(dir)}")
