first_num = int(input('Please enter first number: '))
second_num = int(input('Please enter second number: '))
i = 1
greatest_divisor_found_yet = 1

while i <= min(first_num, second_num):
    if first_num % i == 0 and second_num % i == 0:
        greatest_divisor_found_yet = i
    i += 1
print('The gcd is:', greatest_divisor_found_yet)
