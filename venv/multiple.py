# Multiple inheritance is when one class inherits from multiple classes , and is able to assess or use attributes and methods from both classes

# Parent class
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_type(self):
        print("The type is in section .".format(self.section))

# Child class
class Shirts(Item, Garment):
    def __int__(self, sku, section, type, name, color):
        # initialize the fields that belong to the child class
        self.name = name
        self.color = color
        # initialize the first class
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale".format(self.color, self.name))

Short = Shirts("00001", 32, "Trouser", "Casual", "White")
Short.print_sku()
Short.print_shirt()
Short.print_type()
