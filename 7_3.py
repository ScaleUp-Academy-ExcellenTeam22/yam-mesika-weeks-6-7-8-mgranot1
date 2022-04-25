
class Message:
    """
    A Message Representation Class

    """
    def __init__(self, title, body, sender, receiver):
        self.title = title
        self.body = body
        self.sender = sender
        self.receiver = receiver

    def __str__(self):
        return 'Message (title=' + self.title + ' ,body=' + self.body + ' ,sender=' + self.sender+ ' ,receiver=' + self.receiver+ ')'

    def __len__(self):
        return len(self.body)
