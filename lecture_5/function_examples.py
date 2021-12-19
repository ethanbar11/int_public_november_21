def sum_and_print(num1, num2):
    print('The first number is', num1, 'and the second one is', num2)
    x = num1 + num2
    print(x)


def count_even_numbers_amount(lst):
    counter = 0
    # len is a function receiving list and returning the amount of items in list.
    # range is a function receiving integer and returning a "list"
    # containing numbers from 0 to this integer -1 (for example
    # receiving 5 makes [0,1,2,3,4]
    for i in range(len(lst)):
        x = lst[i]
        if x % 2 == 0:
            counter = counter + 1

    return counter


just_some_lst = [0, 2, 34, 32124, 324, 32, 4, 23, 4, 23, 43, 24, 234, 12, 24, 12, 4, 12, 34, 12, 3]
even_amount = count_even_numbers_amount(just_some_lst)
print('The amount of even numbers is', even_amount)
# x1 = 50
# print('Starting using function!')
# sum_and_print(4, 'Hello')
