import os
import shutil

# destination
# /Users/ak/workspace/github.com/kadlex-web/static-site-generator/public
# source
# /Users/ak/workspace/github.com/kadlex-web/static-site-generator/static


'''Function given a source directory(str) and a destination directory(str); 
function checks to see if the destination and source exists. if source doesn't exist, function does not execute.
if destination exists - delete old version to ensure clean copy. create new one

Then a helper function copies the source directory and its files into the destination directory'''
def copy_static(source, destination):
    # check to see if source exists
    if os.path.exists(source):
        # checks to see if destination exists
        if os.path.exists(destination):
            print(f"{destination} already exists. i need to delete it")
            shutil.rmtree(destination)
            print(f"deleted!")
            print(f"creating a fresh {destination}")
            os.mkdir(destination)
        else:
            print("you need to create a destination")
            os.mkdir(destination)
            print("created!")

        copy_source_dir(source, destination)

    else:
        raise Exception(f"{source} does not exist. Please provide a working source directory")

def copy_source_dir(source, destination):
    directory_list = os.listdir(source)
    print(directory_list)
    for file in directory_list:
        if file == '.DS_Store':
            pass
        else:
            new_file = os.path.join(destination, file)
            print(new_file)
            source_file = os.path.join(source, file)

            if os.path.isfile(source_file):
                print(f"{source_file} is a file and I need to copy it")
                print(f"copying {source_file} to {new_file}")
                shutil.copy(source_file, destination)
                print("done!")

            else:
                print(f"{file} is a directory. we need to enter the directory to check for files")
                os.mkdir(new_file)
                new_source = os.path.join(source, file)
                print(f"moving to source:{new_source} and destination: {new_file}")
                copy_source_dir(new_source, new_file)


destination = "/Users/ak/workspace/github.com/kadlex-web/static-site-generator/public"
source = "/Users/ak/workspace/github.com/kadlex-web/static-site-generator/static"

copy_static(source, destination)