# def make_letter_opposite(letter):
#     ascii_value = ord(letter)
#     if 65 <= ascii_value <= 90:
#         ascii_value += 32
#     # This means it is a small letter
#     elif 97 <= ascii_value <= 122:
#         ascii_value -= 32
#     else:
#         pass
#     return chr(ascii_value)


def make_lower(letter):
    ascii_value = ord(letter)
    # This means its an upper letter
    if 65 <= ascii_value <= 90:
        ascii_value += 32
    else:
        pass
    return chr(ascii_value)


def make_upper(letter):
    ascii_value = ord(letter)
    # This means its an lower case letter
    if 97 <= ascii_value <= 122:
        ascii_value -= 32
    else:
        pass
    return chr(ascii_value)





# This function accepts string and count the types in it.
def count_types(s):
    types_count = {'big': 0, 'small': 0, 'special': 0, 'digits': 0}
    for letter in s:
        ascii_value = ord(letter)
        if 32 <= ascii_value < 47:
            types_count['special'] = types_count['special'] + 1
        elif 48 <= ascii_value <= 57:
            types_count['digits'] = types_count['digits'] + 1
        elif 65 <= ascii_value <= 90:
            types_count['big'] = types_count['big'] + 1
        elif 97 <= ascii_value <= 122:
            types_count['small'] = types_count['small'] + 1
    return types_count


def print_count_types(s):
    counts = count_types(s)
    for name, amount in counts.items():
        print(name, amount)


def lower_upper(num, s):
    new_s = ''
    if num == 1:
        for letter in s:
            new_s = new_s + make_lower(letter)
    elif num == 2:
        for letter in s:
            new_s = new_s + make_upper(letter)
    print_count_types(s)
    return new_s

print(lower_upper(2, 'ABCD1234***$abcd123'))
# print(make_letter_opposite('z'))
# print(ord('A'))
