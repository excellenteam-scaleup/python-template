"""Module implementing a PostOffice messaging system with inbox management."""

from typing import Any


class PostOffice:
    """
    A Post Office class allowing registered users to send and receive messages.

    :ivar int message_id: Incremental counter of the last message sent.
    :ivar dict[str, list[dict[str, Any]]] boxes: Inboxes mapped by username.
    """

    def __init__(self, usernames: list[str]) -> None:
        """
        Initialize the PostOffice with inboxes for given usernames.

        :param usernames: List of usernames for which to create mailboxes.
        """
        self.message_id: int = 0
        self.boxes: dict[str, list[dict[str, Any]]] = {
            user: [] for user in usernames
        }

    def send_message(
        self,
        sender: str,
        recipient: str,
        message_body: str,
        title: str = "",
        urgent: bool = False,
    ) -> int:
        """
        Send a message to a recipient's mailbox.

        :param sender: The username of the sender.
        :param recipient: The username of the recipient.
        :param message_body: The content body of the message.
        :param title: Optional subject title of the message.
        :param urgent: If True, message is placed at the front of the inbox.
        :return: The auto-incremented unique ID of the sent message.
        :raises KeyError: If the recipient does not exist in the post office.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")

        self.message_id += 1
        message_details: dict[str, Any] = {
            "id": self.message_id,
            "sender": sender,
            "title": title,
            "body": message_body,
            "read": False,
        }

        recipient_box = self.boxes[recipient]
        if urgent:
            recipient_box.insert(0, message_details)
        else:
            recipient_box.append(message_details)

        return self.message_id

    def read_inbox(
        self, username: str, num_messages: int | None = None
    ) -> list[dict[str, Any]]:
        """
        Read unread messages from a user's mailbox and mark them as read.

        :param username: The username whose mailbox will be read.
        :param num_messages: Maximum number of unread messages to retrieve.
                             If None, all unread messages are returned.
        :return: A list of messages marked as read.
        :raises KeyError: If the username does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist.")

        unread_messages = [msg for msg in self.boxes[username] if not msg["read"]]
        messages_to_return = (
            unread_messages
            if num_messages is None
            else unread_messages[:num_messages]
        )

        for message in messages_to_return:
            message["read"] = True

        return messages_to_return

    def search_inbox(
        self, username: str, query: str
    ) -> list[dict[str, Any]]:
        """
        Search for messages in a mailbox matching a query string.

        Searches in both the message title and the message body.

        :param username: The username whose mailbox will be searched.
        :param query: The search string to look for.
        :return: List of all matching messages (read and unread).
        :raises KeyError: If the username does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist.")

        return [
            msg
            for msg in self.boxes[username]
            if query in msg["title"] or query in msg["body"]
        ]


# Aliases to support variations in exercise naming
sent_turtle = PostOffice  # pylint: disable=invalid-name


def main() -> None:
    """Demonstrate PostOffice usage with sample messages."""
    office = PostOffice(["Alice", "Bob"])

    office.send_message("Alice", "Bob", "Hello Bob!", title="Greeting")
    office.send_message(
        "Alice", "Bob", "Project deadline tomorrow", title="Urgent Task", urgent=True
    )

    print("--- Searching Bob's inbox for 'Task' ---")
    search_results = office.search_inbox("Bob", "Task")
    for msg in search_results:
        print(f"Found: {msg['title']} - {msg['body']}")

    print("\n--- Reading first unread message for Bob ---")
    first_read = office.read_inbox("Bob", 1)
    for msg in first_read:
        print(f"Read: {msg['title']}")

    print("\n--- Reading remaining unread messages for Bob ---")
    remaining_read = office.read_inbox("Bob")
    for msg in remaining_read:
        print(f"Read: {msg['title']}")


if __name__ == "__main__":
    main()
