import os
from pathlib import Path


def thats_the_way(folder_path):
    with os.scandir(folder_path) as files:
        return [
            file.name
            for file in files
            if file.is_file() and file.name.startswith("deep")
        ]


if __name__ == "__main__":
    images_folder = Path(__file__).resolve().parent / "images"

    if images_folder.is_dir():
        result = thats_the_way(images_folder)
        print(result)
        print("Matching files:", len(result))  # Expected: 2
    else:
        print("Place the tutorial's 'images' folder next to this file to test it.")
