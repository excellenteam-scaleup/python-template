IMAGE_DIR = '../img/logo.jpg'
MSG_END = '!'


def find_msg(file_name):
    with open(file_name, "rb") as file:
        message = ""

        while True:
            byte = file.read(1)
            if not byte:
                break

            char = chr(byte[0])
            if 'a' <= char <= 'z':
                message += char

            elif char == MSG_END:
                if len(message) >= 5:
                    yield message
                message = ""
            else:
                message = ""


def parsle_tongue():
    for msg in find_msg(IMAGE_DIR):
        print(msg)

if __name__ == '__main__':
    parsle_tongue()