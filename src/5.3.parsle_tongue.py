def parsle_tongue():
    messages = []
    current_message = ""

    with open("resources/logo.jpg", "rb") as file:
        while True:
            data = file.read(1024)

            if not data:
                break

            for byte in data:
                if 97 <= byte <= 122:
                    current_message += chr(byte)

                elif byte == 33:
                    if len(current_message) >= 5:
                        messages.append(current_message + "!")
                    current_message = ""

                else:
                    current_message = ""

    return messages


if __name__ == "__main__":
    print(parsle_tongue())