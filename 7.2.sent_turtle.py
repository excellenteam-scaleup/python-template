class PostOffice:
    """A Post Office class. Allows users to message each other.

    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    # Added 'title' parameter with a default value of "" to support search_inbox without breaking existing code
    def send_message(self, sender, recipient, message_body, title="", urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        message_body : str
            The body of the message.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
        KeyError
            If the recipient does not exist.

        Examples
        --------
        After creating a PO box and sending a letter,
        the recipient should have 1 messege in the
        inbox.

        >>> po_box = PostOffice(['a', 'b'])
        >>> message_id = po_box.send_message('a', 'b', 'Hello!')
        >>> len(po_box.boxes['b'])
        1
        >>> message_id
        1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username: str, n: int = None) -> list:
        """
        Reads the first n messages from the user's inbox.
        If n is not provided, reads all messages. Read messages are removed from the inbox.
        """
        user_box = self.boxes[username]
        read_messages = []
        if n is None:
            n = len(user_box)

        for i in range(n):
            if len(user_box) > 0:
                message = user_box.pop(0)
                read_messages.append(message)

        return read_messages

    def search_inbox(self, username: str, text: str) -> list:
        """Searches for a given text in the titles and bodies of the user's messages"""
        text_inside = []
        user_box = self.boxes[username]
        for message in user_box:
            if text in message['title'] or text in message['body']:
                text_inside.append(message)

        return text_inside


if __name__ == '__main__':

    po_box = PostOffice(['a', 'b'])


    po_box.send_message('a', 'b', 'Are we still on for lunch?') # הודעה ישנה בלי כותרת
    po_box.send_message('a', 'b', 'Please send the report', title='Urgent Report') # הודעה עם כותרת
    po_box.send_message('a', 'b', 'I found a great new restaurant for lunch!', title='Food') # עוד אחת

    print("--- Search for 'lunch' ---")
    search_results = po_box.search_inbox('b', 'lunch')
    for msg in search_results:
        print(msg)

    print("\n--- Read first 2 messages ---")
    read_msgs = po_box.read_inbox('b', 2)
    for msg in read_msgs:
        print(msg)

    print("\n--- Read remaining messages ---")
    remaining = po_box.read_inbox('b')
    for msg in remaining:
        print(msg)