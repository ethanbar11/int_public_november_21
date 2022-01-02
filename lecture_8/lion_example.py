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


zoo12 = Zoo()
zoo12.add_lion('Shlomi')
