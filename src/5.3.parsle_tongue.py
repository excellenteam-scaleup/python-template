"""Module for extracting hidden messages from a binary file.
"""

from collections.abc import Generator

CHUNK_SIZE = 1024
MIN_MESSAGE_LENGTH = 5


def parsle_tongue(file_path: str) -> Generator[str, None, None]:
    """Yield secret messages of 5+ lowercase letters ending with '!'."""
    current_word: list[str] = []

    try:
        with open(file_path, "rb") as binary_file:
            while chunk := binary_file.read(CHUNK_SIZE):
                for byte in chunk:
                    if ord("a") <= byte <= ord("z"):
                        current_word.append(chr(byte))
                    elif (
                            byte == ord("!")
                            and len(current_word) >= MIN_MESSAGE_LENGTH
                    ):
                        current_word.append("!")
                        yield "".join(current_word)
                        current_word.clear()
                    else:
                        current_word.clear()
    except FileNotFoundError:
        print(f"Error: {file_path} not found")


def main() -> None:
    """Read the logo path from user input and print yielded messages."""
    file_path = input("Enter file path: ").strip().strip('"')

    for message in parsle_tongue(file_path):
        print(message)


if __name__ == "__main__":
    main()