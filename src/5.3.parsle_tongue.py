
from pathlib import Path
from typing import Iterator


def parsle_tongue(file_path: str) -> Iterator[str]:
    """Yield secret messages found in a binary file."""
    message = bytearray()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            for byte in chunk:
                if 97 <= byte <= 122:
                    message.append(byte)

                elif byte == 33:
                    if len(message) >= 5:
                        yield message.decode("ascii")
                    message.clear()

                else:
                    message.clear()


if __name__ == "__main__":
    logo_path = Path(__file__).resolve().parent.parent / "resources" / "logo.jpg"

    for secret_message in parsle_tongue(str(logo_path)):
        print(secret_message)
