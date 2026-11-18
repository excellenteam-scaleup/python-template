from PIL import Image
from pathlib import Path



def decode_message(image_path):
    message = ""

    with Image.open(image_path) as image:
        image = image.convert("RGB")
        width, height = image.size

        for x in range(width):
            for y in range(height):
                if image.getpixel((x, y)) == (1, 1, 1):
                    message += chr(y)
                    break

    return message


if __name__ == "__main__":
    image_file = Path(__file__).resolve().parent / "resources" / "code.png"
    print(decode_message(image_file))