height = int(input('Please enter your height:'))
age = int(input('Please enter your age:'))
if 8 < age < 18:
    if height > 115:
        print('You are allowed!')
    else:
        print('Nope')
elif age > 18 and height > 100:
    print('You are allowed!')
else:
    print('Nopy nope.')
