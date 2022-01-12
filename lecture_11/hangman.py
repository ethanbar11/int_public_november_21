import random


# This is a function that receives words.txt file path and returns
# a random word.
def get_random_word(path):
    with open(path, 'r') as words_file:
        lines = words_file.readlines()

        # Because of the fact that the lines contain \n which is a symbol
        # for 'enter', I remove from each line.
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')

        # Choosing a random line inside the file.
        index_of_word = random.randint(0, len(lines) - 1)

        # Going through all the lines and removes from each one
        # if it contains '\n' the '\n' in it.
        return lines[index_of_word]


class ScoreBoard:
    # The scoreboard accepts a path of the scoreboard on the hard disk.
    # If the path is None, a new file is created.
    def __init__(self, path):
        self.path = path

        # Maximal rows in the score board.
        self.max_size = 3
        # This is a dictionary that contains name:amount pairs which is the scoreboard.
        self.scores = {}

        # Im reading the current file for the current score board.
        try:
            with open(path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line.replace('\n', '')
                    # Splits the line where the comma is, to name, and guesses amount
                    values = line.split(',')
                    # Im doing it because values = ['Eliran',5] => values[0]=Eliran, values[1]=5
                    name = values[0]
                    amount = int(values[1])
                    self.scores[name] = amount
        except FileNotFoundError as e:
            self.scores = {}

    # This function accepts name and guesses amount, and checks if the name is in the top 3
    # participants of the game. if so, it drops the worse participant and adds this one.
    # else, does nothing.
    def update_scoreboard(self, name, guesses_amount):

        # Checks if the scoreboard is not full yet.
        if len(self.scores) < self.max_size:
            # If its not full, insert the name:guesses
            self.scores[name] = guesses_amount
            self.update_file()
        else:
            # If its full
            min_guesses_in_score = 6
            min_guesses_in_score_name = None

            # Finds the row with the lowest guesses amount.
            for name, guesses in self.scores.items():
                if guesses < min_guesses_in_score:
                    min_guesses_in_score = guesses
                    min_guesses_in_score_name = name

            # Checks if the new row should enter to the scoreboard.
            if min_guesses_in_score < guesses_amount:
                # if so, deletes the old row
                del self.scores[min_guesses_in_score_name]
                # and inserts the new one.
                self.scores[name] = guesses_amount
                self.update_file()

    # This functions takes the current scores dictionary and save it to the file.
    def update_file(self):
        with open(self.path, 'w') as file:
            # This is how you iterate throguh dictionary.
            for name, guesses in self.scores.items():
                line = '{},{}\n'.format(name, guesses)
                file.write(line)

    def print_scores(self):
        for name, guesses in self.scores.items():
            print(name, guesses)


class HangmanSession:
    def __init__(self, word, score_board):
        self.word_to_guess = word
        self.guesses_left = 5
        self.letters_already_guessed = []
        self.score_board = score_board

    def perform_session(self):
        print('The word is:')
        self.print_hangman_word()
        win = False
        while self.guesses_left > 0 and win == False:
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
        if win:
            print('Well done, the game has ended succesfully.')
            name = input('Please enter your name: ')
            self.score_board.update_scoreboard(name, self.guesses_left)
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


should_continue = True
my_score_board = ScoreBoard('./score_board.txt')
while should_continue:
    choice = input('Do you want to 1) play a game 2) see score board 3) exit.')
    if choice == '1':
        word = get_random_word(r'words.txt')
        session = HangmanSession(word, my_score_board)
        session.perform_session()
    elif choice == '2':
        # Shows score board.
        my_score_board.print_scores()
    elif choice == '3':
        should_continue = False
    else:
        print('I dont know what you want.')
