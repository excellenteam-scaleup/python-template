"""Module for finding files starting with a specific prefix."""

import os

TARGET_PREFIX = "deep"


def thats_the_way(folder_path: str) -> list[str]:
    """
    Find all files in a directory that start with the prefix 'deep'.

    :param folder_path: Path to the target directory.
    :return: List of filenames starting with 'deep'.
    :raises FileNotFoundError: If folder_path does not exist or is not a directory.
    """
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Directory not found: {folder_path}")

    return [
        filename
        for filename in os.listdir(folder_path)
        if filename.startswith(TARGET_PREFIX)
        and os.path.isfile(os.path.join(folder_path, filename))
    ]


def main() -> None:
    """Run demonstration for thats_the_way function."""
    current_directory = "."
    matched_files = thats_the_way(current_directory)
    print(f"Files starting with '{TARGET_PREFIX}': {matched_files}")


if __name__ == "__main__":
    main()
