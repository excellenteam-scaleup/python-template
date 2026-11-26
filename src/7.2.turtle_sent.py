
"""Manage a post office and its users' messages."""


class PostOffice:
    """Allow users to send, read and search messages."""

    def __init__(self, usernames):
        """Create an inbox for each user."""
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body,
                     urgent=False, subject=""):
        """Send a message and return its unique ID."""
        user_box = self.boxes[recipient]
        self.message_id += 1

        message = {
            "id": self.message_id,
            "body": message_body,
            "sender": sender,
            "subject": subject,
            "read": False
        }

        if urgent:
            user_box.insert(0, message)
        else:
            user_box.append(message)

        return self.message_id

    def read_inbox(self, username, number=None):
        """Return unread messages and mark them as read."""
        unread = [
            message for message in self.boxes[username]
            if not message["read"]
        ]

        selected = unread[:number]

        for message in selected:
            message["read"] = True

        return selected

    def search_inbox(self, username, text):
        """Return messages containing text in subject or body."""
        return [
            message for message in self.boxes[username]
            if text in message["subject"]
            or text in message["body"]
        ]


def turtle_sent():
    """Demonstrate the post office operations."""
    office = PostOffice(["Alice", "Bob"])

    office.send_message(
        "Alice", "Bob", "Hello Bob!", subject="Greeting"
    )

    office.send_message(
        "Alice", "Bob", "Meeting tomorrow", subject="Meeting"
    )

    print("First read:")
    print(office.read_inbox("Bob", 1))

    print("Remaining unread messages:")
    print(office.read_inbox("Bob"))

    print("Search results:")
    print(office.search_inbox("Bob", "Meeting"))

    print("Unread messages:")
    print(office.read_inbox("Bob"))


if __name__ == "__main__":
    turtle_sent()
