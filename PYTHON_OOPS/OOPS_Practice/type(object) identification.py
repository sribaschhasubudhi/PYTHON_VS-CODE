'''IMPORTANT'''
# Write a Python program that creates objects from multiple classes and uses the built-in type() function to identify which class each object belongs to.

class Dog:
    pass

class Cat:
    pass

d=Dog()
c=Cat()
print(type(d))              
print(type(c))
print(type(d).__name__)     #Shows only the name of class
print(type(c).__name__)