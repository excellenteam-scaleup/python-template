from pathlib import Path
from PIL import Image


def remember_remember(file_path: str) -> str:
    """Decode a hidden message from an image."""
    image = Image.open(file_path)
    width, height = image.size

    message = []

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))

            if pixel == 0:
                message.append(chr(y))
                break

            if pixel == (0, 0, 0):
                message.append(chr(y))
                break

            if pixel == (0, 0, 0, 255):
                message.append(chr(y))
                break

    return "".join(message)


if __name__ == "__main__":
    image_path = Path(__file__).resolve().parent.parent / "resources" / "code.png"
    print(remember_remember(str(image_path)))