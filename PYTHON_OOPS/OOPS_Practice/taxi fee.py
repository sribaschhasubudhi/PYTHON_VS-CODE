# Write a Python program that creates a Vehicle parent class with a base fare, 
# then extends a Taxi child class that adds a 10% maintenance fee on top of the base fare using super().

class Vehicle:
    def __init__(self,base_fare):
        self.base_fare=base_fare

    def total_fare(self):
        print(f"Total fare:- ₹{self.base_fare}")

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintenance_fee=0.1*self.base_fare
        self.base_fare+=self.maintenance_fee

yellow=Taxi(100)
yellow.total_fare()