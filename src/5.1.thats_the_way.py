from glob import glob

SERCH_DEEP = "deep*"

def thats_the_way(path_name:str):
    return glob(SERCH_DEEP, root_dir=path_name)

if __name__ == "__main__":
    print(thats_the_way("../../webDevClass/img"))