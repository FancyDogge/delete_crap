import os
import argparse

def get_files(folder_path, file_extension):
    if not os.path.exists(folder_path):
        raise Exception(f"The folder {folder_path} does not exist!")

    matching_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(file_extension) and os.path.isfile(f"{folder_path}/{filename}"):
            matching_files.append(os.path.join(folder_path, filename))
    return matching_files

def delete_files(file_list):
    for file_path in file_list:
        try:
            os.remove(file_path)
            print(f"File '{file_path}' was deleted.")
        except OSError as e:
            print(f"Error deleting file '{file_path}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Delete files based on a specified extension.")
    parser.add_argument("folder", help="Path to the folder where files will be deleted.")
    parser.add_argument("extension", help="File pattern to match extension of the file (e.g., .txt).")
    args = parser.parse_args()

    folder_path = args.folder
    file_pattern = args.extension

    matching_files = get_files(folder_path, file_pattern)

    if not matching_files:
        print(f"No files found in '{folder_path}' matching the pattern '{file_pattern}'.")
        return

    print(f"Files to be deleted:")
    for file_path in matching_files:
        print(f"---> {file_path}")

    user_confirm = input("Do you want to proceed? (y/n): ").lower()

    if user_confirm == "y":
        delete_files(matching_files)
        print("Deletion complete.")
    else:
        print("Deletion canceled.")

if __name__ == "__main__":
    main()