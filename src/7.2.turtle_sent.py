
from collections.abc import Iterable
from typing import Any


class PostOffice:
    """Manage users' mailboxes and support sending and reading messages."""

    def __init__(self, usernames: Iterable[str]) -> None:
        """Create an empty inbox for each username."""
        self.message_id = 0
        self.boxes: dict[str, list[dict[str, Any]]] = {
            username: [] for username in usernames
        }

    def send_message(
        self,
        sender: str,
        recipient: str,
        message_body: str,
        urgent: bool = False,
        subject: str = "",
    ) -> int:
        """Send a message and return its unique ID.

        Args:
            sender: Username of the sender.
            recipient: Username of the recipient.
            message_body: Content of the message.
            urgent: Place the message first if True.
            subject: Optional message subject.

        Returns:
            The ID of the new message.

        Raises:
            KeyError: If the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1

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

    def read_inbox(
        self,
        username: str,
        n: int | None = None,
    ) -> list[dict[str, Any]]:
        """Return unread messages and mark them as read.

        Args:
            username: Owner of the inbox.
            n: Maximum number of messages to read.
                If None, read all unread messages.

        Returns:
            A list of messages that were read.

        Raises:
            KeyError: If the username does not exist.
            ValueError: If n is negative.
        """
        if n is not None and n < 0:
            raise ValueError("Number of messages cannot be negative.")

        unread_messages = [
            message
            for message in self.boxes[username]
            if not message["read"]
        ]

        messages_to_read = (
            unread_messages if n is None else unread_messages[:n]
        )

        for message in messages_to_read:
            message["read"] = True

        return [message.copy() for message in messages_to_read]

    def search_inbox(
        self,
        username: str,
        query: str,
    ) -> list[dict[str, Any]]:
        """Find messages containing a string in the subject or body.

        Args:
            username: Owner of the inbox.
            query: Text to search for.

        Returns:
            All matching messages, including previously read ones.

        Raises:
            KeyError: If the username does not exist.
        """
        query = query.lower()

        return [
            message.copy()
            for message in self.boxes[username]
            if query in message["subject"].lower()
            or query in message["body"].lower()
        ]


if __name__ == "__main__":
    post_office = PostOffice(["Alice", "Bob"])

    post_office.send_message(
        "Alice", "Bob", "Hello Bob!", subject="Greeting"
    )
    post_office.send_message(
        "Alice", "Bob", "Python is awesome", subject="Python"
    )
    post_office.send_message(
        "Alice", "Bob", "Urgent meeting", urgent=True
    )

    print("Test 1 - Read one message:")
    print(post_office.read_inbox("Bob", 1))

    print("\nTest 2 - Read remaining messages:")
    print(post_office.read_inbox("Bob"))

    print("\nTest 3 - Read again:")
    print(post_office.read_inbox("Bob"))

    print("\nTest 4 - Search for Python:")
    print(post_office.search_inbox("Bob", "python"))

    print("\nTest 5 - Search for greeting:")
    print(post_office.search_inbox("Bob", "greeting"))

    print("\nTest 6 - Assertions:")
    assert post_office.read_inbox("Bob") == []
    assert len(post_office.search_inbox("Bob", "python")) == 1
    assert post_office.read_inbox("Alice") == []
    print("All tests passed!")
