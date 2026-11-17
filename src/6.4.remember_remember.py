from PIL import Image

def remember_remember(path):
    img = Image.open(path).convert("RGB")
    width, height = img.size
    message = ""

    for x in range(width):
        for y in range(height):
            if not img.getpixel((x, y)) == (255, 255, 255):
                message += chr(y)
                break

    return message


if __name__ == "__main__":
    print(remember_remember("../img/code.png"))