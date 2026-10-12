'''IMPORTANT'''
# Write a Python program that defines an Animal base class with an eat() method, 
# creates a few subclasses, 
# and builds a Zoo class that holds a list of animals and calls eat() on all of them via a feed_all() method.

class Animal:                               # Animal is the parent class
    # Constructor method:-
    def __init__(self,animal,food):
        self.animal=animal
        self.food=food

    def eat(self):
        return f"{self.animal} eats {self.food}"

class Lion(Animal):                         # Lion is an Animal
    # Constructor method:-
    def __init__(self, animal, food):
        super().__init__(animal, food)
        pass                                # Lion iherits the eat() of Animal

class Deer(Animal):
    # Constructor method:-
    def __init__(self, animal, food):
        super().__init__(animal, food)
        pass

class Parrot(Animal):
    # Constructor method:-
    def __init__(self, animal, food):
        super().__init__(animal, food)
        pass

class Zoo:                      # Zoo HAS Animals (Composition)
    def __init__(self):
        self.animals=[]

    def add_animal(self,animal):
        self.animals.append(animal)

    # Polymorphism magic:-
    def feed_all(self):
        for i in self.animals:
            print(i.eat()) 

''' i is the object of child class. all the child classes (Lion,Deer,Parrot) 
    inherits the eat() from the parent class 'Animal'. When i doesn't finds the eat()
    in any of the child class, it, by polymorphism, moves to the parent class.
    Animal, the parent class has the eat() method. So, i now becomes the object of Animal
    class and calls the eat() method.'''    
        
z=Zoo()
z.add_animal(Lion("Lion","meat"))
z.add_animal(Deer("Deer","grass"))
z.add_animal(Parrot("Parrots","chillies"))
z.feed_all()
