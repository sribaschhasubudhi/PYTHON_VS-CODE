# Write a Python program that defines a Vehicle base class and creates Bike and Truck subclasses, 
# each defining a unique max_speed attribute and a describe() method.

class Vehicle:
    def __init__(self):
        pass

class Bike(Vehicle):
    def __init__(self,name,max_speed):
        super().__init__()
        self.name=name
        self.max_speed=max_speed

    def describe(self):
        print(f"max speed of {self.name} is {self.max_speed}km/h")

class Truck(Vehicle):
    def __init__(self,name,max_speed):
        super().__init__()
        self.name=name
        self.max_speed=max_speed

    def describe(self):
        print(f"max speed of {self.name} is {self.max_speed}km/h")

bike=Bike("Harley-Davidson Street 750",175)
bike.describe()
truck=Truck("Volvo Iron Knight",271)
truck.describe()