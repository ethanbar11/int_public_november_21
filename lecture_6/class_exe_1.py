def bulletproof_input():
    is_valid = False
    value = None
    while not is_valid:
        try:
            value = int(input('Please enter value: '))
            if 1 <= value <= 10000:
                is_valid = True
            else:
                print('The value is not in the right range')
        except ValueError:
            print('The value is not correct!')
    return value


print('The value you entered is:', bulletproof_input())
