
class Message:
    """
    A Message Representation Class

    """
    def __init__(self, title: str , body: str, sender: str, receiver: str):
        self.title = title
        self.body = body
        self.sender = sender
        self.receiver = receiver

    def __str__(self):
         return 'Message (title= {} ,body= {} ,sender= {} ,receiver= {} )'.format(self.title, self.body, self.sender,self.receiver)


    def __len__(self):
        return len(self.body)
