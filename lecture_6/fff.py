num=int(input('enter a number between 1 and 10,000 '))
if 1<=num<=10000:
    print(num)
else:
    try:
        num()
    except ValueError(num):
        print('your number is out of range, please try again')
