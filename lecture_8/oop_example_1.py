class Item:
    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code

    def printInfo(self):
        print('Name : {} Price : {} code : {}'.format(self.name, self.price, self.code))

    # def sum(self,num1,num2):
    #     Sums num1,num2 and returns the value


milk = Item('Milk', 50, 11)
milk.printInfo()

microwave=Item('Microwave',1000,12)
microwave.printInfo()

# sum_of_numbers=microwave.sum(1,2)