class LetterBox:
    def __init__(self):
        self.FlagUp = bool
        self.letter = ''

    def take_letter(self):
        if self.FlagUp:
            return self.letter
        if not self.FlagUp:
            print("No letters")

    def insert_letter(self, letter):
        if not self.FlagUp:
            self.letter = letter
        if self.FlagUp:
            print("One must read before they can write")



