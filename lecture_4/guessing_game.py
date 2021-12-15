import random

bottom = int(input('Please enter lower bound:'))
top = int(input('Please enter upper bound:'))
x = random.randint(bottom, top)

is_number_found = False
while not is_number_found:
    guess = int(input('Please enter a number between 1 and 100: '))
    if guess < x:
        print('Too low!')
    elif guess > x:
        print('Too high!')
    else:
        is_number_found = True

print('You found the number! good job.')
