from letter_box import LetterBox
from alice import Alice
from bob import Bob
from letter import Letter



def main():

    alice_letter_box = LetterBox()
    bob_letter_box = LetterBox()
    bob = Bob(bob_letter_box)
    alice = Alice(alice_letter_box)

    bob.send_letter(alice, "hi")
    alice.get_letter(alice)




