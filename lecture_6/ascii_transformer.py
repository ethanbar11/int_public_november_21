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


def lower_upper(num, s):
    new_s = ''
    if num == 1:
        for letter in s:
            new_s = new_s + make_lower(letter)
    elif num == 2:
        for letter in s:
            new_s = new_s + make_upper(letter)
    return new_s

print(lower_upper(2,'Hello MYAGKafaef234124;;f'))
# print(make_letter_opposite('z'))
# print(ord('A'))
