"""Module for decoding hidden text messages from black pixels in an image.
"""

from PIL import Image

DARK_PIXEL_THRESHOLD = 128
DEFAULT_IMAGE_PATH = "resources/code.png"


def remember_remember(image_path: str) -> str:
    """Return the hidden message from black pixels."""
    decoded_chars: list[str] = []

    try:
        with Image.open(image_path) as raw_image:
            image = raw_image.convert("L")
            width, height = image.size
            for col in range(width):
                for row in range(height):
                    if image.getpixel((col, row)) < DARK_PIXEL_THRESHOLD:
                        decoded_chars.append(chr(row))
                        break
    except FileNotFoundError:
        print(f"Error: {image_path} not found")
        return ""

    return "".join(decoded_chars)


def main() -> None:
    """Read image path or use default and print the message."""
    user_path = input(
        f"Enter image path (Enter for {DEFAULT_IMAGE_PATH}): "
    ).strip().strip('"').strip("'")
    target_path = user_path or DEFAULT_IMAGE_PATH
    print(remember_remember(target_path))


if __name__ == "__main__":
    main()