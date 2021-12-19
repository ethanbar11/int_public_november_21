def special_print(s, number):
    if number == 0:
        print(s.upper())
    elif number == 1:
        print(s.lower())
    else:
        print('NO!!')
    return 5



s = input('Please enter string:')
number = int(input('Please enter choice:'))
print(special_print(s, number))
