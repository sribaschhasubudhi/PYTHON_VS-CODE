# Write a Python program that defines a Shape base class with an area() method, 
# then implements it in Circle, Square, and Triangle subclasses using the appropriate geometric formulas.

class Shape:
    def __init__(self):
        self.shape="shape"

    def area(self):
        if self.shape=="circle":
            ar=round(3.14*(self.r**2),2)
            print(f"Area of the {self.shape} is {ar} sq.m")

        if self.shape=="square":
            ar=round(self.s**2,2)
            print(f"Area of the {self.shape} is {ar} sq.m")

        if self.shape=="triangle":
            ar=round(0.5*(self.b*self.h),2)
            print(f"Area of the {self.shape} is {ar} sq.m")

class Circle(Shape):
    def __init__(self,r):
        super().__init__()
        self.shape="circle"
        self.r=r

class Square(Shape):
    def __init__(self,s):
        super().__init__()
        self.shape="square"
        self.s=s

class Triangle(Shape):
    def __init__(self,b,h):
        super().__init__()
        self.shape="triangle"
        self.b=b
        self.h=h

cir=Circle(3.6)
cir.area()
squ=Square(5.4)
squ.area()
tri=Triangle(2.7,5.1)
tri.area()