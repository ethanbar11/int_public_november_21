# i = 2
# while i < 1000:
#     print(i)
#     i += 2
#
# # Second version
# while i < 1000:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# num = int(input('Please enter a number:'))
# if num % 2 == 0 and 100 <= num <= 350:
#     print('Goody good')
# else:
#     print('Baddy bad.')


low = int(input('Please enter lower bound: '))
high = int(input('Please enter higher bound: '))
if low < high:
    while low < high:
        print(low)
        low += 1
else:
    print('Your input is not valid.')
