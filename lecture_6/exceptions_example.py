def inner_3():
    raise TypeError('Woho')


def inner_2():
    inner_3()


def inner():
    inner_2()

try:
    inner_2()
except TypeError:
    print('ffff')
# try:
#     x = 3 / 0
#     #
# except ZeroDivisionError:
#     print('I divided by 0. Very bad!')
# except TypeError:
#     print('Tried to do something wrong')
# except Exception:
#     print('Everything else.')
# print('Everything continued.')
