class PostOffice:
    """A simple post office that manages a mailbox for each user.

    Each message is stored as a dict with the keys:
        id      - unique running message number
        title   - message subject (may be an empty string)
        body    - message text
        sender  - username of the sender
        read    - True once the recipient has read the message
    """

    def __init__(self, usernames):
        """Create an empty mailbox for every username in `usernames`."""
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False, title=''):
        """Send a message to `recipient` and return its id.

        Urgent messages are placed at the start of the mailbox,
        regular messages at the end.
        `title` is optional (default empty) so existing calls keep working.
        """
        user_box = self.boxes[recipient]
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

    def read_inbox(self, user, n=None):
        """Return the first `n` unread messages in `user`'s mailbox.

        If `n` is not given (None), return all unread messages.
        Returned messages are marked as read, so they will not be
        returned again by the next call.
        """
        unread = [message for message in self.boxes[user] if not message['read']]
        if n is not None:
            unread = unread[:n]
        for message in unread:
            message['read'] = True
        return unread

    def search_inbox(self, user, text):
        """Return a list of all messages in `user`'s mailbox whose
        title or body contains `text`.

        Searches both read and unread messages and does not change
        their read status.
        """
        return [
            message for message in self.boxes[user]
            if text in message['title'] or text in message['body']
        ]


if __name__ == '__main__':
    post = PostOffice(['alice', 'bob'])
    post.send_message('bob', 'alice', 'Hello Alice', title='Greeting')
    post.send_message('bob', 'alice', 'Meeting at 10', title='Work')
    post.send_message('bob', 'alice', 'Server is down!', urgent=True, title='Alert')

    # Urgent message should come first (expected: id 3)
    print('Read 1 message:', post.read_inbox('alice', 1))

    # Remaining unread messages (expected: ids 1, 2)
    print('Read the rest:', post.read_inbox('alice'))

    # Nothing left to read (expected: [])
    print('Read again:', post.read_inbox('alice'))

    # Search in title (expected: id 2)
    print("Search 'Work':", post.search_inbox('alice', 'Work'))

    # Search in body, including read messages (expected: id 1)
    print("Search 'Alice':", post.search_inbox('alice', 'Alice'))

    # No match (expected: [])
    print("Search 'nothing':", post.search_inbox('alice', 'nothing'))

    # Empty mailbox (expected: [])
    print("Search bob's inbox:", post.search_inbox('bob', 'Hello'))
