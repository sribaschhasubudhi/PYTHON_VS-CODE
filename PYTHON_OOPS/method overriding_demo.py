class Animal():
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):            #Parent class(Animal) method overrided
        super().sound()         #Parent method called
        print("Dogs bark")

d=Dog()
d.sound()