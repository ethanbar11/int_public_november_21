class Item:
    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code

    def printInfo(self):
        print('Name : {} Price : {} code : {}'.format(self.name, self.price, self.code))


milk = Item('Milk', 50, 11)
milk.printInfo()

microwave=Item('Microwave',1000,12)
microwave.printInfo()
