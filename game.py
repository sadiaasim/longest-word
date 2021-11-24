# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
class Game:
    """
    Game Class for generating random letters and getting words for validation.
    Also keep a check two ways
    """
    def __init__(self):
        """
        Initializing the game with a random grid
        """
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        """
        Method determines if the word is validation
        """
        if word == '':
            return False
        counter = 0
        for letter in word:
            if str(self.grid).find(letter) != -1 and \
                    str(self.grid).count(letter) >= word.count(letter):
                counter += 0
            else:
                counter += 1
        if counter == 0 :
            return True
        return False
