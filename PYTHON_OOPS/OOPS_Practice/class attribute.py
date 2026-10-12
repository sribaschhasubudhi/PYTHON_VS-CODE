'''IMPORTANT'''

# Write a Python program to create a Vehicle class with a class attribute color = "White" that is shared by all instances. 
# Create two vehicle objects and demonstrate that both share the same default color. 
# Show that changing the class attribute updates all instances that have not overridden it.

class Vehicle:
    colour="White"                  # This is a class attribute

    def __init__(self,car,speed):
        self.car=car
        self.speed=speed
        # car and speed are instance attributes

v1=Vehicle("TATA",200)
v2=Vehicle("Mahindra",190)
print(f"Default colour of every car:-{Vehicle.colour}")
# v1.colour and v2.colour also have the same value as Vehicle.colour
print(" ")

print(f"{v1.car}- Colour: {v1.colour}, Speed: {v1.speed}")
print(f"{v2.car}- Colour: {v2.colour}, Speed: {v2.speed}")
print(" ")
Vehicle.colour="Black"              # Class Attribute changed

print(f"{v1.car}- Colour: {v1.colour}, Speed: {v1.speed}")
print(f"{v2.car}- Colour: {v2.colour}, Speed: {v2.speed}")