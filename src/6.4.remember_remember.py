
"""Decode a hidden message from an image."""

from PIL import Image


def remember_remember(file_path):
    """Return the hidden message in the image."""
    message = []

    with Image.open(file_path) as image:
        image = image.convert("RGB")
        width, height = image.size

        for x in range(width):
            for y in range(height):
                if max(image.getpixel((x, y))) < 128:
                    message.append(chr(y))
                    break

    return "".join(message)


if __name__ == "__main__":
    print(remember_remember("resources/code.png"))
