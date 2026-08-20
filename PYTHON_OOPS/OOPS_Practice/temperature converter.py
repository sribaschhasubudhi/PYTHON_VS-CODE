# Write a Python program to create a Temperature class that stores a temperature in Celsius. 
# Add two methods: to_fahrenheit() that converts and returns the value in Fahrenheit, and to_kelvin() that converts and returns the value in Kelvin.

class Temperature:
    def __init__(self):
        self.celsius=float(input("Enter the temperature in Celsius:-"))

    def to_fahrenheit(self):
        fah=(1.8*self.celsius)+32
        print(f"{self.celsius}˚C = {fah}˚F")

    def to_kelvin(self):
        kel=self.celsius+273
        print(f"{self.celsius}˚C = {kel} K")

temp=Temperature()
temp.to_fahrenheit()
temp.to_kelvin()