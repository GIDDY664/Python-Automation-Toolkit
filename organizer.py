import os
import shutil

# Replace this with a path to a test folder on your computer
target_folder = r"C:\Users\user\OneDrive\Desktop\Test"

# Get a list of all files in the folder
files= os.listdir(target_folder)


    
for file in files:
    # 1. Clean up the extension name (remove the dot and make lowercase)
    filename, extension = os.path.splitext(file)
    extension = extension[1:].lower()

    # 2. Skip folders or files with no extension
    if extension== "":
        continue

    # 3. Create the path for the new folder
    new_folder_path = os.path.join(target_folder, extension)

    # 4. Create the folder if it's not already there
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # 5. Move the file into the new folder
    shutil.move(os.path.join(target_folder, file), os.path.join(new_folder_path, file))

    print(f"success: Moved {file} to the {extension} folder!")