from pathlib import Path


def parsle_tongue(image_path, chunk_size=4096):
    """Yield lowercase messages of at least five letters ending in '!'."""
    letters = bytearray()

    with open(image_path, "rb") as image:
        while chunk := image.read(chunk_size):
            for char in chunk:
                if 97 <= char <= 122:  # a-z
                    letters.append(char)
                elif char == 33:  # !
                    if len(letters) >= 5:
                        yield letters.decode("ascii") + "!"
                    letters.clear()
                else:
                    letters.clear()


if __name__ == "__main__":
    image_file = Path(__file__).resolve().parent / "images" / "logo.jpg"

    if image_file.is_file():
        for message in parsle_tongue(image_file):
            print(message)
    else:
        print("Put resources/logo.jpg next to this script's folder.")
