"""Exercise 5.1: Find files whose names start with 'deep'."""

import os


def thats_the_way(dir_path: str) -> list[str]:
    """Return names of files starting with 'deep' in the given directory."""
    files = os.listdir(dir_path)
    result = []

    for file in files:
        if file.startswith("deep"):
            if os.path.isfile(os.path.join(dir_path, file)):
                result.append(file)

    return result


if __name__ == "__main__":
    pass
