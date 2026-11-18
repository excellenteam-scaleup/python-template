"""Extend the course's PostOffice with inbox reading and searching."""


class PostOffice:
    """Manage inboxes for registered usernames and deliver messages.

    Args:
        usernames (iterable): Names of users who have an inbox.

    Attributes:
        message_id (int): ID of the most recently sent message.
        boxes (dict): Lists of messages for each registered user.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False, subject=""):
        """Send a message and return its incrementing ID.

        Args:
            sender (str): Sender's name.
            recipient (str): Existing recipient's username.
            message_body (str): Message text.
            urgent (bool): Insert urgent messages at the front of the inbox.
            subject (str): Optional subject; added for searching.

        Raises:
            KeyError: If the recipient is not registered.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            "id": self.message_id,
            "body": message_body,
            "sender": sender,
            "subject": subject,
            "read": False,
        }

        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)

        return self.message_id

    def read_inbox(self, username, N=None):
        """Return up to N unread messages in inbox order and mark them read.

        Args:
            username (str): Existing inbox owner.
            N (int, optional): Maximum messages to read; all if omitted.

        Returns:
            list: Messages read by this call.

        Raises:
            KeyError: If username is not registered.
            ValueError: If N is negative.
        """
        if N is not None and N < 0:
            raise ValueError("N must be non-negative")

        unread = [message for message in self.boxes[username] if not message["read"]]
        selected = unread[:N]

        for message in selected:
            message["read"] = True

        return selected

    def search_inbox(self, username, search_string):
        """Return all messages containing text in their subject or body.

        The search ignores case and includes previously read messages.

        Args:
            username (str): Existing inbox owner.
            search_string (str): Text to search for.

        Returns:
            list: Messages matching the search text.

        Raises:
            KeyError: If username is not registered.
        """
        query = search_string.casefold()
        return [
            message
            for message in self.boxes[username]
            if query in message["subject"].casefold()
            or query in message["body"].casefold()
        ]


if __name__ == "__main__":
    office = PostOffice(["Daniel", "Adel"])

    first_id = office.send_message("Daniel", "Adel", "Hi!")
    second_id = office.send_message("Daniel", "Adel", "Project meeting", subject="Meeting")
    urgent_id = office.send_message("Daniel", "Adel", "Urgent news", True)

    assert (first_id, second_id, urgent_id) == (1, 2, 3)
    assert [message["id"] for message in office.boxes["Adel"]] == [3, 1, 2]
    assert [message["id"] for message in office.read_inbox("Adel", 1)] == [3]
    assert [message["id"] for message in office.read_inbox("Adel")] == [1, 2]
    assert office.read_inbox("Adel") == []
    assert [message["id"] for message in office.search_inbox("Adel", "MEETING")] == [2]

    print("All PostOffice tests passed.")
