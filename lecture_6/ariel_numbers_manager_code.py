import random

l = []

print("initiate a list")
randomness_range = int(input("enter random max value: "))
items_in_list = int(input("enter how many items in list: "))


def clr_pop_lst(lst):
    count = 0
    lst.clear()
    while count < items_in_list:
        lst.append(random.randrange(randomness_range))
        count += 1
    print("\nlist cleared and populated with", items_in_list, "random numbers\n")


def show_lst_min_max(lst):  # without using min() max()
    min1 = lst[0]
    max1 = 1
    for i in lst:
        if i < min1:
            min1 = i
        elif i > min1:
            if max1 < i:
                max1 = i

    print("min: ", min1)
    print("max: ", max1)


def add_value(lst, val):
    lst.append(val)
    print(val, "was added to end of list")


def sort_lst(lst):  # without using - sort(lst)
    lst1 = lst.copy()
    sortedlst = []
    while lst1:
        min1 = lst1[0]
        for i in lst1:
            if i < min1:
                min1 = i
        lst1.remove(min1)
        sortedlst.append(min1)

    print("the sorted list: ", sortedlst)


def lst_avrg(lst):  # without sum and average methods
    sum1 = 0
    for n in lst:
        sum1 += n
    avrg1 = sum1 / len(lst)
    print("average is: ", avrg1)


def locate_num(lst, num):
    index = False
    for i in range(len(lst)):
        if lst[i] == num:
            index = True
        else:
            continue
    if index:
        print("locate_num:", num, "is in list index", i)
    else:
        print("locate_num:", num, "isn't in the list")


def count_num(lst, num):
    num_in_lst = False
    count = 0
    for i in lst:
        if i == num:
            count += 1
            num_in_lst = True
    if num_in_lst:
        print("count_num: the number", num, "appears", count, "in the list")
    else:
        print("count_num: The number", num, "isn't in the list")


def lst_delta(lst):
    delta_lst = [*range(randomness_range)]
    for i in delta_lst:
        if i in lst:
            delta_lst.remove(i)
    print("lst_delta: ", delta_lst)


def choose_option():
    print("\nPlease select one of the following options: "
          "\n 1 show list min and max "
          "\n 2 add values into list "
          "\n 3 sort list "
          "\n 4 calculate average of list "
          "\n 5 locate number's index within list "
          "\n 6 chose a number and display how many times it appears in the list "
          "\n 7 display all the numbers that are not in the list (within it's range) "
          "\n 8 exit ")
    option = int(input())
    if option == 0:
        clr_pop_lst(l)
    elif option == 2:
        add_value(l, 3)
    elif option == 1:
        show_lst_min_max(l)
    elif option == 4:
        lst_avrg(l)
    elif option == 5:
        locate_num(l, 3)
    elif option == 6:
        count_num(l, 3)
    elif option == 3:
        sort_lst(l)
    elif option == 7:
        lst_delta(l)
    return option


clr_pop_lst(l)
while choose_option() <= 7:
    print("original random list", l)