# Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. Create an object of the class and print both attributes.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

    def vroom(self):
        print(f"With a speed of {self.max_speed}km/h and {self.mileage}km/L; this car gives a deadly combo")

car=Vehicle(250,11)
car.vroom()