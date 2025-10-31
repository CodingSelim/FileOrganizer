import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isdir(full_path):
            continue  # Skip directories
        name, extension = os.path.splitext(item)
        extension = extension.lower().strip('.')

        if extension == "":
            extension = "others"

        target_folder = os.path.join(folder_path, f'{extension}_files')
        os.makedirs(target_folder, exist_ok=True)

        new_path = os.path.join(target_folder, item)
        shutil.move(full_path, new_path)

        print(f'Moved: {item} → {target_folder}')

    print("\n All files have been organized successfully!")

if __name__ == "__main__":
    path = input("Enter the path of the folder to organize: ")
    organize_folder(path)

