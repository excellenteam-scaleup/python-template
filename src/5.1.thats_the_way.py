import os


def thats_the_way(folder):
    result = []

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)

        if os.path.isfile(full_path) and file.startswith("deep"):
            result.append(file)

    return result


if __name__ == "__main__":
    print(thats_the_way("img"))
