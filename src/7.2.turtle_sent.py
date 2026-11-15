class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        user_box = self.boxes[recipient]
        self.message_id += 1

        message_details = {
            "id": self.message_id,
            "body": message_body,
            "sender": sender,
        }

        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)

        return self.message_id

    def read_inbox(self, username, n):
        inbox = self.boxes[username]
        messages = inbox[:n]
        del inbox[:n]
        return messages

    def search_inbox(self, username, keyword):
        inbox = self.boxes[username]

        return [
            message for message in inbox
            if keyword in message["body"]
            or keyword in message["sender"]
        ]


if __name__ == "__main__":
    post_office = PostOffice(["Alice", "Bob"])

    post_office.send_message("Alice", "Bob", "Hello Bob!")
    post_office.send_message("Alice", "Bob", "Python is fun")
    post_office.send_message("Alice", "Bob", "Hello again!")

    print(post_office.search_inbox("Bob", "Hello"))
    print(post_office.read_inbox("Bob", 2))
    print(post_office.boxes["Bob"])
    