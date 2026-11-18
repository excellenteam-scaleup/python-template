"""PostOffice exercise: send, read and search messages in user mailboxes."""


class PostOffice:
    """A post office that manages a mailbox for each user.

    Each message is a dict with the keys:
    id, title, body, sender and read.
    """
    def __init__(self, usernames):
        """Create an empty mailbox for every user.

        :param usernames: Iterable of usernames
        """
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def _get_box(self, user):
        """Return the mailbox of a user.

        :param user: Username whose mailbox is needed
        :return: The user's list of messages
        :raises ValueError: If the user does not exist
        """
        if user not in self.boxes:
            raise ValueError(f"Unknown user: {user}")
        return self.boxes[user]

    def send_message(self, sender, recipient, message_body, urgent=False, title=''):
        """Send a message to a user's mailbox.

        Urgent messages are placed at the start of the mailbox,
        regular messages at the end.

        :param sender: Username of the sender
        :param recipient: Username of the recipient
        :param message_body: Text of the message
        :param urgent: True to put the message at the start of the mailbox
        :param title: Title of the message (default empty)
        :return: The id of the new message
        :raises ValueError: If the recipient does not exist
        """
        user_box = self._get_box(recipient)
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user, count=None):
        """Return the first count unread messages and mark them as read.

        Messages that were already read are not returned again.

        :param user: Username whose mailbox is read
        :param count: Number of messages to read; None reads all unread messages
        :return: List of the read messages
        :raises ValueError: If the user does not exist
        """
        unread = [message for message in self._get_box(user) if not message['read']]
        if count is not None:
            unread = unread[:count]
        for message in unread:
            message['read'] = True
        return unread

    def search_inbox(self, user, text):
        """Return all messages whose title or body contains the given text.

        Searches read and unread messages without changing their status.

        :param user: Username whose mailbox is searched
        :param text: The text to search for
        :return: List of matching messages
        :raises ValueError: If the user does not exist
        """
        return [
            message for message in self._get_box(user)
            if text in message['title'] or text in message['body']
        ]


if __name__ == '__main__':
    post = PostOffice(['alice', 'bob'])
    post.send_message('bob', 'alice', 'Hello Alice', title='Greeting')
    post.send_message('bob', 'alice', 'Meeting at 10', title='Work')
    post.send_message('bob', 'alice', 'Server is down!', urgent=True, title='Alert')

    print('Read 1 message:', post.read_inbox('alice', 1))
    print('Read the rest:', post.read_inbox('alice'))
    print('Read again:', post.read_inbox('alice'))
    print("Search 'Work':", post.search_inbox('alice', 'Work'))
    print("Search 'Alice':", post.search_inbox('alice', 'Alice'))
    print("Search 'nothing':", post.search_inbox('alice', 'nothing'))
    print("Search bob's inbox:", post.search_inbox('bob', 'Hello'))

    try:
        post.read_inbox('charlie')
    except ValueError as error:
        print('Error:', error)
