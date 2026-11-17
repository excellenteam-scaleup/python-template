import os


def thats_the_way(folder_path: str) -> list[str]:
    files = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path) and filename.startswith("deep"):
            files.append(filename)

    return files


print(thats_the_way("images"))