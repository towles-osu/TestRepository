# Author:
# Date:
# Description:

import random

cw = open('crosswords.txt', 'r')
word_list = []
for word in cw:
    word_list.append(word.rstrip('\n')) )

    # print(word_list)
    number_of_guesses = 8

    # 2) A function that allows the executioner to pick a random word and tells the crowd how many letters are in it


class Hangman:

    def __init__(self):
        self._word = random.choice(word_list)
        self._word_length = len(self._word)
        self._fails = 0
        self._display_word = []
        for letter in self._word:
            self._display_word.append("_")

    def get_word(self):
        return self._display_word

    def print_current_word(self):
        """
        Prints current word with dashes for unguessed letters.
        """
        print(self.get_word().join(' '))

    def check_letter(self, letter):
        """checks if a letter is in the word"""
        for temp_letter in self._word:
            if temp_letter == letter:
                return True
        return False

    def update_display_word(self, letter):
        """updates a list that is the display word with the letter added in"""
        # assumes display word is a list of letters with '_' for blanks
        for position in range(len(self._display_word)):
            if self._word[position] == letter:
                self._display_word[position] = letter

    def play_hangman(self, limit_guesses):
        """this function starts a game of hangman"""
        while self._fails < limit_guesses:
            current_letter = self.pick_letter().lower()
            if self.check_letter(current_letter):
                self.update_display_word(current_letter)
                # maybe more stuff happens when they guess right
            else:
                self._fails += 1

    # word_to_guess = pick_word()
    # 3) A function that asks the players to guess a letter
    def pick_letter():
        """
        Allows user to choose a letter.
        """
        print("Pick a letter. Choose wisely. Clippy.exe's life depends on it.")
        letter = input()
        return letter


# Executioner's greeting
print("Welcome to the execution of Clippy.exe!")


# 4) A function that determines what happens when the players guess a letter right

# 5) A function that determines what happens when the players guess a letter wrong


# 6) A function that determines what happens when "Sticky.exe" is hung

def game_is_lost():
    print("You have chosen poorly, it's the end of the line for Clippy.exe")


# 7) A function that determines what happens if "Sticky.exe" gets to run free

# 8) A function that asks if the players want to play again, and ends the program if no

if __name__ == "__main__":
    response = 'Y'
    while (response != "N"):
        response = input("Play again? Y/N")
        hangman = Hangman()

    print("Thanks for playing Hangman!")