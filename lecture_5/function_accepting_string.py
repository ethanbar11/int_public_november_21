def print_twice(s):
    print(s, s)


def bla():
    print('woho')


# This means- run the code below the if only if I ran this file.
# If i imported this file - don't run what under the if.
if __name__ == '__main__':
    print_twice('Hello')