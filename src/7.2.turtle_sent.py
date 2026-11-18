
class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False, title=''):
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
        unread = [message for message in self.boxes[user] if not message['read']]
        if n is not None:
            unread = unread[:n]
        for message in unread:
            message['read'] = True
        return unread

    def search_inbox(self, user, text):
        return [
            message for message in self.boxes[user]
            if text in message['title'] or text in message['body']
        ]

def turtle_sent():
    pass

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
