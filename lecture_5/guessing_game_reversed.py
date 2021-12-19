import math

is_guessed_correctly = False
low = 1
high = 100

while not is_guessed_correctly:  # same as: while is_guessed_correctly==False
    # What floor does is making floor(5.2) =5, floor(10.9)=10
    guess = math.floor((high + low) / 2)  # Same as int()
    print('My guess is :', guess)
    guess_response = input('Is my guess correct? ')
    if guess_response == 'too high':
        high = guess - 1
    elif guess_response == 'too low':
        low = guess + 1
    elif guess_response == 'exactly':
        print('I guessed correctly! finishing.')
        is_guessed_correctly = True
    else:
        print('Bad response, exiting.')
        is_guessed_correctly = True
