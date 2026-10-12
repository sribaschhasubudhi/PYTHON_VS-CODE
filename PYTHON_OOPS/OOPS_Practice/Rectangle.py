# Write a Python program to create a Rectangle class with length and width as instance attributes, and two methods: area() that returns the area and perimeter() that returns the perimeter.
from dataclasses import dataclass

@dataclass
class Rectangle:
    length:int
    width:int

    def area(self):
        ar=self.length*self.width
        print(f"The area of the rectangle is {ar}")

    def perimeter(self):
        peri=2*(self.length+self.width)
        print(f"The perimeter of the rectangle is {peri}")

rec=Rectangle(3,5)
rec.area()
rec.perimeter()