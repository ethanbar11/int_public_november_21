class Bird:
    pass


# Crow inherits bird
class Crow(Bird):
    pass


class Lion:
    def __init__(self, name):
        self.my_name = name

    def rawr(self):
        print('Rawr :{}'.format(self.my_name))

    def __str__(self):
        return 'The lion name is ' + self.my_name


class Zoo:
    def __init__(self):
        self.lions_in_zoo = {}

    def add_lion(self, lion_name):
        new_lion = Lion(lion_name)
        self.lions_in_zoo[lion_name] = new_lion

    def delete_lion(self, lion_name):
        if lion_name not in self.lions_in_zoo:
            raise Exception('There is no lion with that name in the zoo!')

        # The syntax of deleting item in dictionary by the key.
        del self.lions_in_zoo[lion_name]

    def count(self):
        print('The lion amount is: {}'.format(len(self.lions_in_zoo)))

    def print_lions(self):
        for lion in self.lions_in_zoo.values():
            print(lion)

    def print_longest_lion_name(self):
        if len(self.lions_in_zoo) == 0:
            raise Exception('Cannot get longest name if the amount is 0!!!!')
        longest_name_found = None
        longest_name_length = -1
        for lion in self.lions_in_zoo:
            if len(lion.my_name) > longest_name_length:
                longest_name_length = len(lion.my_name)
                longest_name_found = lion.my_name
        print('The longest lion name is:', longest_name_found)


zoo12 = Zoo()
# for i in range(5):
#     name = input('Please enter lion name:')
#     zoo12.add_lion(name)
zoo12.add_lion('Shlomi11111111111111111')
zoo12.add_lion('Shlomi2')
zoo12.add_lion('Shlomi3')
zoo12.add_lion('Shlomi4')
zoo12.add_lion('Shlomi332135')
zoo12.print_lions()
print(zoo12)  # inside the print function - It calls the function __str__

# zoo12.count()
# zoo12.print_longest_lion_name()
