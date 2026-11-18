"""Module for filtering files starting with 'deep' in a given folder path.
"""

import os


def thats_the_way(folder_path: str) -> list[str]:
    """Return all file names in folder_path that start with 'deep'."""
    return [
        name
        for name in os.listdir(folder_path)
        if name.startswith("deep")
        and os.path.isfile(os.path.join(folder_path, name))
    ]


if __name__ == "__main__":
    user_folder = input("Enter folder path: ")
    result = thats_the_way(user_folder)
    print(result)