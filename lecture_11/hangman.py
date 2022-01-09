import random


# This is a function that receives words file path and returns
# a random word.
def get_random_word(path):
    with open(path, 'r') as words_file:
        lines = words_file.readlines()
        index_of_word = random.randint(0, len(lines) - 1)
        return lines[index_of_word]

print(get_random_word(r'words'))