"""Module for extracting hidden secret messages from binary files."""

from collections.abc import Iterator
import os

CHUNK_SIZE = 1024
MIN_MESSAGE_LENGTH = 5
EXCLAMATION_MARK = "!"


def parsle_tongue(file_path: str) -> Iterator[str]:
    """
    Extract hidden secret messages from a binary file using a generator.

    A secret message consists of at least 5 lowercase English letters
    ending with an exclamation mark.

    :param file_path: Path to the binary file.
    :return: Generator yielding each found secret message.
    :raises FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    current_chars: list[str] = []

    with open(file_path, "rb") as binary_file:
        while chunk := binary_file.read(CHUNK_SIZE):
            for byte in chunk:
                char = chr(byte)
                if "a" <= char <= "z":
                    current_chars.append(char)
                elif char == EXCLAMATION_MARK:
                    if len(current_chars) >= MIN_MESSAGE_LENGTH:
                        yield "".join(current_chars) + EXCLAMATION_MARK
                    current_chars.clear()
                else:
                    current_chars.clear()


def main() -> None:
    """Demonstrate parsle_tongue on a sample binary file if available."""
    sample_path = "resources/logo.jpg"
    if os.path.isfile(sample_path):
        for message in parsle_tongue(sample_path):
            print(f"Found message: {message}")
    else:
        print(f"Sample file '{sample_path}' not found. Test with an existing file.")


if __name__ == "__main__":
    main()
