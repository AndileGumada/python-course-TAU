# inheritance is when a child class can use attributes and methods of a parent class

class Person():
    def __init__(self, fname, lname, health, status):
        self.fname = fname
        self.lname = lname
        self.health = health
        self.status = status


class Andile(Person):
    def __init__(self, weapon, employeed):
        # we use  super() to refer to the attributes of a parent class in subclass
        super().__init__(fname, lname, health, status)
        # use self to initialize the new attributes
        self.weapon = weapon
        self.employeed = employeed

def hurt(self, other):

    if self.weapon == 'rock':
        # Python Decrement Operator
        other.health -= 10
    elif self.weapon == 'stick':
        other.health -= 5
    print(other, health)


def insult(self, other):

    if other.health <= 80:
        print("{}, you are tired and weak".format(other.fname))

def steal(self, other):
    print("Ha ha ha, {}, I have your stuff!".format(other,fname))

    if other.status == True:
        other.status = False
Andile = Person('rock','Andile',76, status= False)
