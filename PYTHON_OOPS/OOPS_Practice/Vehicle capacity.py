'''IMPORTANT'''
# Write a Python program where a Vehicle parent class has a seating_capacity() method that accepts a capacity argument. 
# Create a Bus child class that overrides this method to provide a default seating capacity of 50, using super() to call the parent’s version internally.

class Vehicle:
    def seating_capacity(self,capacity):
        print(f"The bus has a capacity of {capacity}")

class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)    # Calling parent class method in a child class method

volvo=Bus()
volvo.seating_capacity()