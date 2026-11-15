import os


def thats_the_way(folder):
    files = os.listdir(folder)
    result = []

    for file in files:
        if file.startswith("deep"):
            result.append(file)

    return result


if __name__ == "__main__":
    print(thats_the_way("images"))
