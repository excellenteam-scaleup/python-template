"""Extract hidden lowercase messages from a binary (image) file."""

IMAGE_PATH = '../img/logo.jpg'
MSG_END = '!'
MIN_MSG_LENGTH = 5


def find_msg(file_name):
    """Yield hidden messages found in a binary file.

    A message is a run of at least 5 lowercase English letters
    that ends with the "!" character.

    :param file_name: Path of the file to scan
    :return: Generator of the hidden messages (str)
    """
    with open(file_name, "rb") as file:
        message = ""

        while byte := file.read(1):
            char = chr(byte[0])
            if 'a' <= char <= 'z':
                message += char

            elif char == MSG_END:
                if len(message) >= MIN_MSG_LENGTH:
                    yield message
                message = ""
            else:
                message = ""


def parsle_tongue():
    """Print every hidden message found in the logo image."""
    for msg in find_msg(IMAGE_PATH):
        print(msg)


if __name__ == '__main__':
    parsle_tongue()
