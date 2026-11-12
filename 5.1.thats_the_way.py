# this file we are doing the mission 5.1 thats the way
# also there are small excrises in the documents, it will apear in the file but with #
#
# for example : small ex
#diffrent_option = ['one', 'two', 'three']
#choose = random.choice(diffrent_option)
#print(choose)


###########3 thats the way ################
import os


def get_directory() -> str:
    """This func is getting a path of a folder"""
    path = input("Enter a folder path: ")
    return path


def thats_the_way(prefix : str, folder_path : str) -> list:
    """Returns a list of files in folder_path that start with prefix."""
    files_with_prefix = []
    try:
        for file_name in os.listdir(folder_path):
            full_item_path = os.path.join(folder_path, file_name)
            if os.path.isfile(full_item_path) and file_name.startswith(prefix):
                files_with_prefix.append(file_name)
    except FileNotFoundError:
        print("Folder do not exist")
    except PermissionError:
        print("you do not have permission  to enter")
    except Exception as e:
        print(f"Unknown error: {e}")
    return files_with_prefix


if __name__ == '__main__':
    folder_path = get_directory()
    prefix = 'deep'

    match_files = thats_the_way(prefix, folder_path)
    print(f"matching files: ", match_files)