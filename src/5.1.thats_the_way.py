"""Find files whose names start with "deep" in a given directory."""

from glob import glob

SEARCH_DEEP = "deep*"
IMG_DIR = "../../webDevClass/img"

def thats_the_way(path_name: str):
    """Return the names of files in a directory that start with "deep".

    :param path_name: Path of the directory to search in
    :return: List of matching file names, relative to path_name
    """
    return glob(SEARCH_DEEP, root_dir=path_name)


if __name__ == "__main__":
    print(thats_the_way(IMG_DIR))
