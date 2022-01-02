class Lion:
    def __init__(self, name):
        self.my_name = name

    def rawr(self):
        print('Rawr :{}'.format(self.my_name))


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


zoo12 = Zoo()
zoo12.add_lion('Shlomi')
