from textnode import *
import os
import shutil

def copy_contents(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    for file in os.listdir(source):
        from_path = os.path.join(source, file)
        to_path = os.path.join(dest, file)
        print(f"Copying {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_contents(from_path, to_path)

def main():
    source = "static"
    dest = "public"
    if os.path.exists(dest):
        shutil.rmtree(dest)
    copy_contents(source, dest)



if __name__ == "__main__":
    main()
