"""Find files in a given directory."""

from pathlib import Path


def thats_the_way(folder_path):
    """Return names of files starting with 'deep'."""
    folder = Path(folder_path)

    return sorted(
        file.name
        for file in folder.iterdir()
        if file.is_file() and file.name.startswith("deep")
    )


if __name__ == "__main__":
    print(thats_the_way("images"))
