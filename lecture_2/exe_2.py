option = input('Please enter c for Celcius and f for Farenheit')
degrees = int(input('Please enter the amount of degrees to convert:'))
if option == 'c':
    new_degrees = (5 / 9) * degrees + 32 * (5 / 9)
    print('The converted degrees are:', new_degrees)
elif option == 'f':
    new_degrees = degrees * (9 / 5) + 32
    print('The converted degrees are:', new_degrees)
else:
    print('You didnt enter one of the options, cant do nothing.')
