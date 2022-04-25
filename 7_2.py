

class PostOffice:
    """A Post Office class. Allows users to message each other.

       :ivar int message_id: Incremental id of the last message sent.
       :ivar dict boxes: Users' inboxes.

       :param list usernames: Users for which we should create PO Boxes.
       """
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

                :param str sender: The message sender's username.
                :param str recipient: The message recipient's username.
                :param str message_body: The body of the message.
                :param urgent: The urgency of the message.
                :type urgent: bool, optional
                :return: The message ID, auto incremented number.
                :rtype: int
                :raises KeyError: if the recipient does not exist.
                """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, usernames, N=-1):
        """Reading the first N messages of the user.

                :param str usernames: The username of the box owner.
                :param N: Number of messages to read.
                :type N: int, optional
                :return: first N messages in the user's box.
                :rtype: list
                :raises KeyError: if the recipient does not exist.
                """
        if N == -1:
            return_messages = [message for message in self.boxes[usernames] if message['read'] == False]
            for message in self.boxes[usernames]:
                message['read'] = True
            return return_messages

        return_messages = [self.boxes[usernames][i] for i in range(len(self.boxes[usernames])) if
                           i < N and self.boxes[usernames][i]['read'] == False]
        for i in range(len(self.boxes[usernames])):
            if i < N:
                self.boxes[usernames][i]['read'] = True
        return return_messages

    def search_inbox(self, usernames, str_for_search):
        """Look for messages that contain a str_for_search.

                        :param str usernames: The username of the box owner.
                        :param str str_for_search: String for checking if messages contain it
                        :return: Messages in the user's box which conains the string to search.
                        :rtype: list
                        :raises KeyError: if the recipient does not exist.
                        """
        return [message for message in self.boxes[usernames] if
                message['sender'].find(str_for_search) != -1 or message['body'].find(str_for_search) != -1]


