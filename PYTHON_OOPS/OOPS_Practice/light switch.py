# Write a Python program to create a Light class with three methods: 
# turn_on() that switches the light on, 
# turn_off() that switches it off, 
# and status() that reports whether the light is currently on or off.

class Light:
    def __init__(self):
        self.switch=input("Do you want to turn on or off? :-")

    def turn_on(self):
        if self.switch=="on":
            status="on"
            print(f"Switch is {self.switch}")

    def turn_off(self):
        if self.switch=="off":
            status="off"
            print(f"Switch is {self.switch}")

    def status(self):
        if self.switch=="on":
            print(f"Status: Light bulb is glowing")
        else:
            print(f"Status: Light bulb is not glowing")

bulb=Light()
bulb.turn_on()
bulb.turn_off()
bulb.status()