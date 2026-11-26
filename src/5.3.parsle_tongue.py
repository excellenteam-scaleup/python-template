
"""Extract hidden messages from a binary file."""


def parsle_tongue(file_path):
    """Yield hidden messages from a binary file."""
    message = ""

    with open(file_path, "rb") as file:
        while True:
            byte = file.read(1)

            if not byte:
                break

            if b"a" <= byte <= b"z":
                message += byte.decode("ascii")
            elif byte == b"!":
                if len(message) >= 5:
                    yield message + "!"

                message = ""
            else:
                message = ""


if __name__ == "__main__":
    for secret in parsle_tongue("resources/logo.jpg"):
        print(secret)
