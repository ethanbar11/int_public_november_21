import string


# This function encrypts one letter to Ceaser code.
def encrypt_letter(letter, amount=1):
    string_that_contains_letter = None

    # Checking if letter is lower case.
    if letter in string.ascii_lowercase:
        string_that_contains_letter = string.ascii_lowercase
    elif letter in string.ascii_uppercase:
        string_that_contains_letter = string.ascii_uppercase
    else:
        return letter
    index = string_that_contains_letter.index(letter)
    new_index = (index + amount) % len(string_that_contains_letter)
    return string_that_contains_letter[new_index]


# This function receives string and returns an encrypted string
# in this amount.
def encrypt(s, amount=1):
    encrypted_s = ''
    for letter in s:
        encrypted_letter = encrypt_letter(letter, amount)
        encrypted_s += encrypted_letter
    return encrypted_s


def decrypt(s, amount=1):
    return encrypt(s, -1 * amount)


def encrypt_file(path, encrypted_path='encrypted_file.txt', amount=1):
    with open(path, 'r') as old_file:
        with open(encrypted_path, 'w') as new_file:
            old_text = old_file.read()
            encrypted_text = encrypt(old_text, amount)
            new_file.write(encrypted_text)


def decrypt_file(file_to_decrypt, amount=1):
    encrypt_file(file_to_decrypt, 'decrypted_file.txt', (-1) * amount)


file_name = input('Please enter file name:')
amount_to_enter = int(input('Please enter amount:'))
to_encrypt = input('Please enter 1 to encrypt or 2 to decrypt')
if to_encrypt == '1':
    encrypt_file(file_name, amount=amount_to_enter)
elif to_encrypt == '2':
    decrypt_file(file_name, amount_to_enter)
