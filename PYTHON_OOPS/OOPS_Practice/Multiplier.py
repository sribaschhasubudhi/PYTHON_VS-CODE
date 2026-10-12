# Write a Python program that creates a Multiplier class which stores a factor, and 
# implements __call__ so that an instance of the class can be invoked directly like a function to multiply a given number by that factor.

class Multiplier:
    # Constructor Method:-
    def __init__(self,factor):
        self.factor=factor
        pass

    # Object Calling Method:-
    def __call__(self,value):       
        return self.factor * value

m=Multiplier(7)
print(m(8))