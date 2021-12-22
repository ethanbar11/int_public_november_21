def make_letter_opposite(letter):
    ascii_value = ord(letter)
    if 65 <= ascii_value <= 90:
        ascii_value += 32
    # This means it is a small letter
    elif 97 <= ascii_value <= 122:
        ascii_value -= 32
    else:
        pass
    return chr(ascii_value)

print(make_letter_opposite('z'))
# print(ord('A'))
