## First way to print Fibonnaci
# amount = int(input('Please enter amount of numbers to print:'))
#
# last = 1
# current = 1
# counter = 2
# print(last)
# print(current)
# while counter < amount:
#     sum_of_last_and_current = last + current
#     last = current
#     current = sum_of_last_and_current
#     counter += 1
#     print(current)

# Second way to print Fibonnaci
amount = int(input('Please enter amount of numbers to print:'))

# This is a list that will contain the Fibonnaci series.
fib = [1, 1]
counter = 2
while counter < amount:
    sum_of_last_and_current = fib[-1] + fib[-2]
    fib.append(sum_of_last_and_current)
    counter += 1  # Same as counter=counter+1

print(fib)
