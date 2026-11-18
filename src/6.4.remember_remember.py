"""Decode a secret message hidden in the pixels of an image."""

from PIL import Image

WHITE = (255, 255, 255)


def remember_remember(path):
    """Decode a message hidden in an image.

    For each column, the row of the first non-white pixel is the
    ASCII value of the next character in the message.

    :param path: Path of the image file
    :return: The decoded message
    """
    img = Image.open(path).convert("RGB")
    width, height = img.size
    message = ""

    for x in range(width):
        for y in range(height):
            if img.getpixel((x, y)) != WHITE:
                message += chr(y)
                break

    return message


if __name__ == "__main__":
    print(remember_remember("../img/code.png"))
