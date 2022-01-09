import random


# This is a function that receives words file path and returns
# a random word.
def get_random_word(path):
    with open(path, 'r') as words_file:
        lines = words_file.readlines()
        index_of_word = random.randint(0, len(lines) - 1)
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
        return lines[index_of_word]


class HangmanSession:
    def __init__(self, word):
        self.word_to_guess = word
        self.guesses_left = 5
        self.letters_already_guessed = []

    def perform_session(self):
        print('The word is:')
        self.print_hangman_word()
        win = False
        while self.guesses_left > 0:
            letter = input('Please enter a letter:')
            if letter in self.letters_already_guessed:
                print('The letter has already been guessed!')
                continue

            if letter not in self.word_to_guess:
                self.guesses_left -= 1
                print('Bad guess! you have still {} guesses'.format(self.guesses_left))
            else:
                print('Good guess!')
            self.letters_already_guessed.append(letter)
            self.print_hangman_word()
            if self.is_completed_guess():
                print('Woho! success in guessing!')
                win = True
                break
        if win:
            print('Well done, the game has ended succesfully.')
        else:
            print('You are a loser!!!!')

    def print_hangman_word(self):
        word_to_print = ''
        for letter in self.word_to_guess:
            if letter in self.letters_already_guessed:
                word_to_print += ' ' + letter
            else:
                word_to_print += ' ' + '_'

        print(word_to_print)

    def is_completed_guess(self):
        is_completed = True

        # Going through all the letters in the original word
        for letter in self.word_to_guess:

            # if there is letter in the original word that has not already been gussed,
            # Mark the boolean as false.
            if letter not in self.letters_already_guessed:
                is_completed = False

        # If i didn't find any letter that is not contained letters_already_guessed,
        # the boolean is still true.
        return is_completed

    def guess_letter(self, letter):
        if letter in self.letters_already_guessed:
            raise ValueError('The letter has already been guessed.')


word = get_random_word(r'words')
session = HangmanSession(word)
session.perform_session()
