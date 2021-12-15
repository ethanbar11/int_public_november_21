option = 1
while option > 0:
    option = int(input('Please enter option 1-4.'))
    if option != 0:
        num1 = int(input('Please enter first number:'))
        num2 = int(input('Please enter second number:'))
        result = 500
        if option == 1:
            result = num1 + num2
        elif option == 2:
            result = num1 - num2
        elif option == 3:
            result = num1 * num2
        elif option == 4:
            result = num1 / num2
        print('The result is',result)

print('Calculator finished.')