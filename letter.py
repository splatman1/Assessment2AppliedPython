import datetime


class Letter:
    def __init__(self, message = None):
        self.content = message
        self.is_read = bool
        self.date = datetime.date


    def create_letter(self, message):
        self.content = message
        self.date = datetime.date
        self.is_read = False

    def read_letter(self):
        print(self.content)
        self.is_read = True


