"""Module implementing the PostOffice class with inbox reading and search.
"""

from collections.abc import Iterable
from typing import Any


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.
    :param usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames: Iterable[str]) -> None:
        """Initialize message counter and empty inboxes for each user."""
        self.message_id = 0
        self.boxes: dict[str, list[dict[str, Any]]] = {
            user: [] for user in usernames
        }

    def send_message(
        self,
        sender: str,
        recipient: str,
        message_body: str,
        urgent: bool = False,
    ) -> int:
        """Send a message to a recipient.

        :param sender: The message sender's username.
        :param recipient: The message recipient's username.
        :param message_body: The body of the message.
        :param urgent: The urgency of the message. Urgent messages appear first.
        :return: The message ID, auto incremented number.
        :raises KeyError: If the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details: dict[str, Any] = {
            "id": self.message_id,
            "body": message_body,
            "sender": sender,
            "read": False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(
        self, username: str, count: int | None = None
    ) -> list[dict[str, Any]]:
        """Return and mark as read the first unread messages in inbox."""
        unread = [msg for msg in self.boxes[username] if not msg["read"]]
        to_read = unread if count is None else unread[:count]
        for msg in to_read:
            msg["read"] = True
        return to_read

    def search_inbox(
        self, username: str, wanted_string: str
    ) -> list[dict[str, Any]]:
        """Return messages containing the string in subject or body."""
        return [
            msg
            for msg in self.boxes[username]
            if (
                wanted_string in msg["body"]
                or wanted_string in msg.get("title", "")
            )
        ]


def main() -> None:
    """Test PostOffice sending, reading, and searching messages."""
    office = PostOffice(("Newman", "Mr. Peanutbutter"))
    office.send_message("Mr. Peanutbutter", "Newman", "Hello, Newman.")
    office.send_message("Mr. Peanutbutter", "Newman", "Urgent mail!", True)
    print("Search 'Hello':", office.search_inbox("Newman", "Hello"))
    print("Read 1:", office.read_inbox("Newman", 1))
    print("Read remaining:", office.read_inbox("Newman"))


if __name__ == "__main__":
    main()