"""Module for decoding hidden messages encoded in image pixel coordinates."""

import os
from PIL import Image

WHITE_PIXEL_VALUE = 255


def remember_remember(image_path: str) -> str:
    """
    Decode a secret text message hidden in image pixel vertical coordinates.

    Each column in the image contains a dark pixel whose row index (y)
    corresponds to the ASCII value of the encoded character.

    :param image_path: Path to the encoded image file.
    :return: The decoded secret message as a string.
    :raises FileNotFoundError: If the image file does not exist.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    with Image.open(image_path) as image:
        grayscale_image = image.convert("L")
        width, height = grayscale_image.size
        decoded_characters: list[str] = []

        for x_coord in range(width):
            for y_coord in range(height):
                pixel_value = grayscale_image.getpixel((x_coord, y_coord))
                if pixel_value != WHITE_PIXEL_VALUE:
                    decoded_characters.append(chr(y_coord))
                    break

    return "".join(decoded_characters)


# Alias to support alternate naming
decode_message = remember_remember


def main() -> None:
    """Demonstrate remember_remember with a sample image if available."""
    sample_path = "resources/code.png"
    if os.path.isfile(sample_path):
        decoded = remember_remember(sample_path)
        print(f"Decoded message: {decoded}")
    else:
        print(f"Sample image '{sample_path}' not found.")


if __name__ == "__main__":
    main()
