import random

lst = []


def insert_value(inner_lst):
    val = int(input('Please enter value to insert:'))
    inner_lst.append(val)


keep_running = True


def get_maximum(inner_lst):
    if len(inner_lst) == 0:
        return 'There is no values yet in the list!'
    else:
        maximal_value = -1
        for val in inner_lst:
            if val >= maximal_value:
                maximal_value = val

        return 'The maximal value is ' + str(maximal_value)

s = 'Hello ' + 'World' # ='Hello World'
while keep_running:
    option = int(input('Please enter 1 to insert value or 2 to insert 500 ' +
                       'random values, 3 to get maximal value enter 4 to stop running: '))
    if option == 1:
        insert_value(lst)
    elif option == 2:
        for i in range(500):
            lst.append(random.randint(1, 1000))
    elif option == 3:
        print(get_maximum(lst))
    elif option == 4:
        keep_running = False

# x = [1, 2, 3]
# y = [4, 5, 6]
# z = x
#
#
# def print_address(val):
#     print(id(val))
#
#
# print('X address:')
# print_address(x)
#
# print('y address:')
# print_address(y)
# print('z address:')
# print_address(z)
