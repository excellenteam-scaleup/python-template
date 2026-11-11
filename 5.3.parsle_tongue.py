from typing import Generator


def parsle_tongue(file_path: str) -> Generator[str, None, None]:
    """Generator that reads a binary file in chunks and yields secret messages one by one."""
    current_word = ""
    chunk_size = 1024

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            for byte in chunk:
                char = chr(byte)

                if 'a' <= char <= 'z':
                    current_word += char

                elif char == '!':
                    if len(current_word) >= 5:

                        yield current_word + '!'
                    current_word = ""

                else:
                    current_word = ""


if __name__ == '__main__':
    logo_path = "resources/logo.jpg"

    for secret_msg in parsle_tongue(logo_path):
        print("Found secret message:", secret_msg)
