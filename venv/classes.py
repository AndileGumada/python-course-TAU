# class features
# class variables- used by all methods in the class
# instance variables - specific to the object created
# _init_method which allows every instance of a class to be created with specific parameters - ist like a constructor
# self variable which allows info to be shared easily and efficiently
class Person:
    def __init__(self, firstname, lastname, health, status):
        """
        """
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themself"
        print("Hello my name is {} {}".format(self.firstname, self.lastname))

    # def emote(self):
    #     emotion = range.randrange(1, 3)
    #     if emotion == 1:
    #         print("{} is happy today".format(self.firstname))
    #     elif emotion == 2:
    #         print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today".format(self.firstname))
        elif self.health <= 51:
            print("{} feels unwell .".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Andile = Person("Andile", "Gumada", 80, status=True)
Thabile = Person("Thabile", "Gumada", 90, status=False)
Thabo = Person("Thabo", "Moopa", 78, status=True)

print("{} is my friend? {}".format(Andile.firstname,Andile.status))
print("{} is my friend? {}.".format(Thabile.firstname,Andile.status))

Andile.introduce()
Thabile.introduce()

# inheritance this enemy class inherit from the Person class which is the super class
#
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        # we use  super() to refer to the attributes of a parent class in subclass

        super().__init__(firstname, lastname, health, status)
        # use self to initialize the new attributes
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy")

    def hurt(self, other):
        if self.weapon == 'rock':
            # Python Decrement Operator
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("Ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False

# create objects of the class
Alex = Enemy('rock', 'Alex','Wayne', 70, status=False)
Alex.hurt(Andile)
Alex.insult(Thabile)
Alex.insult(Thabo)
Alex.steal(Andile)
# Not available in the super class object
# Andile.steal(Alex)


