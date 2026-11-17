import random


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False, title=''):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                     Urgent messages appear first.
            title (str, optional): The title of the message.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: if the recipient does not exist.
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

    def read_inbox(self, username, n=None):
        """Read the first unread messages in a user's inbox.

        The messages that are returned are marked as read,
        so they will not be returned again in the next call.

        Args:
            username (str): The user whose inbox should be read.
            n (int, optional): How many messages to read.
                               If not given, all the unread messages are returned.

        Returns:
            list: The unread messages, in the order they appear in the inbox.

        Raises:
            KeyError: if the user does not exist.
        """
        unread = [message for message in self.boxes[username] if not message['read']]
        if n is not None:
            unread = unread[:n]
        for message in unread:
            message['read'] = True
        return unread

    def search_inbox(self, username, text):
        """Find all the messages in a user's inbox that contain some text.

        Both the title and the body of every message are searched,
        whether the message was read or not.

        Args:
            username (str): The user whose inbox should be searched.
            text (str): The text to look for.

        Returns:
            list: All the messages that contain the text.

        Raises:
            KeyError: if the user does not exist.
        """
        return [
            message for message in self.boxes[username]
            if text in message['title'] or text in message['body']
        ]


class Player:
    """A player in the Ortal Kombat game.

    Args:
        name (str): The name of the player.

    Attributes:
        name (str): The name of the player.
        hp (int): Current health points of the player.
        max_hp (int): The health points the player has after a revive.
        exp (int): Experience points of the player.
        level (int): The level of the player. Always 1 in this exercise.
        nemeses (list): Players who killed this player, the last one is the newest.
    """

    MAX_HP = 100
    MIN_DAMAGE_PER_LEVEL = 0
    MAX_DAMAGE_PER_LEVEL = 10

    def __init__(self, name):
        self.name = name
        self.max_hp = Player.MAX_HP
        self.hp = self.max_hp
        self.exp = 0
        self.level = 1
        self.nemeses = []

    def attack(self, other=None):
        """Attack another player and take a random amount of health from them.

        The damage is a random number between MIN_DAMAGE_PER_LEVEL * level
        and MAX_DAMAGE_PER_LEVEL * level, where level is the attacker's level.
        If the attacked player drops to 0 hp or less, they are revived
        and the attacker is added to their nemeses.

        Args:
            other (Player, optional): The player to attack.
                                      If not given, the newest nemesis is attacked.

        Returns:
            int: The damage that was done.

        Raises:
            IndexError: if no player was given and this player has no nemeses.
        """
        if other is None:
            other = self.nemeses[-1]
        damage = random.randint(
            Player.MIN_DAMAGE_PER_LEVEL * self.level,
            Player.MAX_DAMAGE_PER_LEVEL * self.level,
        )
        other.hp = other.hp - damage
        if other.hp <= 0:
            other.die(self)
        return damage

    def die(self, killer):
        """Handle the death of the player: revive them and remember the killer.

        If the killer is already a nemesis, they are moved to the end of the list,
        so they become the newest nemesis.

        Args:
            killer (Player): The player who killed this player.
        """
        if killer in self.nemeses:
            self.nemeses.remove(killer)
        self.nemeses.append(killer)
        self.revive()

    def revive(self):
        """Bring the player's health back to the maximum."""
        self.hp = self.max_hp

    def __str__(self):
        return f"{self.name} (hp: {self.hp}, exp: {self.exp}, level: {self.level})"


post_office = PostOffice(['dana', 'yossi'])
post_office.send_message('yossi', 'dana', 'Are you coming to the party?', title='Party')
post_office.send_message('yossi', 'dana', 'Bring snacks please', title='Snacks')
post_office.send_message('yossi', 'dana', 'The party is cancelled', urgent=True, title='Urgent!')
print([message['title'] for message in post_office.read_inbox('dana', 2)])
print([message['title'] for message in post_office.read_inbox('dana')])
print(post_office.read_inbox('dana'))
print([message['id'] for message in post_office.search_inbox('dana', 'party')])
print([message['id'] for message in post_office.search_inbox('dana', 'Snacks')])

player1 = Player('Scorpion')
player2 = Player('Sub-Zero')
while not player2.nemeses:
    player1.attack(player2)
print(player1)
print(player2)
print([nemesis.name for nemesis in player2.nemeses])
player2.attack()
print(player1)
try:
    player1.attack()
except IndexError:
    print("Scorpion has no nemeses to attack")
