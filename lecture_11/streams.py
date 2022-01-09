import sys


def my_print(text):
    sys.stdout.write(text)
    sys.stdout.write('\n')


x = sys.stdin.read(1)
print('the value of x is:', x)
# my_print('Hello World!')
# my_print('This is the second line')

# sys.stdout.write('Hello World!')
# sys.stderr.write('Hello World! #2')
# x = sys.stdin.read(10)
# print(x)
