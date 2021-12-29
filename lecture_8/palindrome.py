def is_palindrome(s):
    new_s = s.replace(' ', '')
    return new_s == new_s[::-1]

print(is_palindrome('abc'))



# s=' Hello my name is Ethannnnn'
# print(s.replace('n','x'))