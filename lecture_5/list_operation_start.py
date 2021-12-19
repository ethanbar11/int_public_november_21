import random

lst = []

keep_running = True

while keep_running:
    option = int(input('Please enter 1 to insert value or 2 to insert 500 ' +
                       'random values, 3 to get maximal value enter 4 to stop running: '))
    if option == 1:
        val = int(input('Please enter value to insert:'))
        lst.append(val)
    elif option == 2:
        for i in range(500):
            lst.append(random.randint(1, 1000))
    elif option == 3:
        if len(lst) == 0:
            print('There is no values yet in the list!')
        else:
            maximal_value = -1
            for val in lst:
                if val >= maximal_value:
                    maximal_value = val
            print('The maximal value is', maximal_value)
    elif option == 4:
        keep_running = False
