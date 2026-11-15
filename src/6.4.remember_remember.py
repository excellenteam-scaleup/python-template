from PIL import Image


def remember_remember(filename):
    image = Image.open(filename).convert("RGB")
    width, height = image.size
    message = ""

    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y))[0] == 1:
                message += chr(y)
                break

    return message


if __name__ == "__main__":
    print(remember_remember("resources/code.png"))