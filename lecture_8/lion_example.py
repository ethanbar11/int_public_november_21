class Lion:
    def __init__(self, name):
        self.my_name = name

    def rawr(self):
        print('Rawr :{}'.format(self.my_name))


class Zoo:
    def __init__(self):
        self.lions_in_zoo = []

    def add_lion(self, lion_name):
        new_lion = Lion(lion_name)
        self.lions_in_zoo.append(new_lion)

    def make_my_lion_rawr(self):
        self.my_lion.rawr()


my_zoo = Zoo('Shlomi')
my_zoo.make_my_lion_rawr()

# Printing the name of the lion inside the zoo.
print(my_zoo.my_lion.my_name)
# x = Lion('Hola')
# x.rawr()
# print(x.sum(1, 2))
