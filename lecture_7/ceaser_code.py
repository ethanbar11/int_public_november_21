import string


def encrypt_letter(letter, amount=1):
    if letter in string.ascii_lowercase:
        index = string.ascii_lowercase.index(letter)
        new_index = (index + amount) % len(string.ascii_lowercase)
        return string.ascii_lowercase[new_index]
    elif letter in string.ascii_uppercase:
        index = string.ascii_uppercase.index(letter)
        new_index = (index + amount) % len(string.ascii_lowercase)
        return string.ascii_uppercase[new_index]
    else:
        return letter


def encrypt(s, amount=1):
    print(s, amount)


print(string.ascii_lowercase, encrypt_letter('z', 13))

# encrypt('Hello')
