# ~Creating parent class: Room()

class Room():
    # Constructor
    def __init__(self,door,window):
        self.door=door
        self.window=window
    def live(self):
        print(f"The house is full of rooms")

# ~Creating child class: Bedroom()

class Bedroom(Room):
    # Constructor
    def __init__(self,door,window,bed):
        # Calling the attributes and methods of Room (parent class)
        super().__init__(door,window)
        self.bed=bed            #Added new argument:- bed
    def sleeping(self):
        print(f"This is my bedroom")

bedroom1=Bedroom(1,4,2)
egroom=Room(2,8)
bedroom1.live()             # Calling parent class(Room) method using child class(Bedroom)
egroom.live()               # Can also be called using parent class(Room)
bedroom1.sleeping()
print(bedroom1.window)
print(f"Extraordinary room with {egroom.door} doors and {egroom.window} windows")
print(f"small bedroom with {bedroom1.door} door and {bedroom1.bed} beds")
print(bedroom1)
print(egroom)
print(Bedroom.mro())
print(isinstance(egroom,Bedroom))       # egroom is not Bedroom 
print(isinstance(bedroom1,Bedroom))     # bedroom1 is a Bedroom
print(issubclass(Bedroom,Room))         # Bedroom is a subclass of Room