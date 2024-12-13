import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if not os.path.isdir(os.path.join(directory, filename)):
            ext = filename.split('.')[-1]
            file = os.path.join(directory, ext)

            if not os.path.exists(file):
                os.makedirs(file)

            shutil.move(os.path.join(directory, filename), os.path.join(file, filename))

if __name__ == "__main__":
    directory = "aula4"
    organize_files(directory)
    print("Done!")
