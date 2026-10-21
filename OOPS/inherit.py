
class Animal:
    def __init__(self,name):
        self.name = name

    def getSound(self):
        print("Generic sound")

class Dog(Animal): #this is how inheritance is done in python
    def getSound(self):
        super().getSound() #super method
        print("Meow")


a1 = Dog("Cat")
a1.getSound()