# Write a Python program that defines an Animal base class with a speak() method, 
# then overrides it in Dog and Cat subclasses to return their respective sounds.

class Animal:
    # Constructor
    def __init__(self,animal,sound):
        self.sound=sound
        self.animal=animal

    def speak(self):
        print(f"{self.animal} says: {self.sound}!")

class Dog(Animal):
    def speak(self):
        super().speak()
        
class Cat(Animal):
    def speak(self):
        super().speak()

owner=Animal("Human","Hello")
rocky=Dog("Dog","woof")
rocky.speak()
pussy=Cat("Cat","meow")
pussy.speak()