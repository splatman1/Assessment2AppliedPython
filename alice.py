from letter_box import LetterBox
from letter import Letter

class Alice:
    def __init__(self, letterbox):
        self.letterbox = letterbox

    def send_letter(self, destination, message):
        letter = Letter(message)
        destination.insert_letter(letter)
    def get_letter(self, destination):
        destination.read_letter()

