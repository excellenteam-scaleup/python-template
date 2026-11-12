from PIL import Image

def decode_message(image_path: str) -> str:
    """Decodes a secret message hidden in the black pixels of an image."""
    img = Image.open(image_path).convert("L")
    width, height = img.size

    message = []
    for x in range(width):
        for y in range(height):
            if img.getpixel((x, y)) == 0:
                message.append(chr(y))
                break

    return "".join(message)


if __name__ == '__main__':
    secret_message = decode_message("resources/code.png")
    print(secret_message)