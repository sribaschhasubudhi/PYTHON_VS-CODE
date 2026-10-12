'''class Car:
    pass
car1=Car()
car2=Car()
print(Car)
print(car1)
print(car2)
# Attributes of Car:-

car1.windows,car1.tyres,car1.engine=4,4,"Petrol"

car2.windows=2
car2.tyres=3
car2.engine="CNG"
print(car1.tyres)
print(car2.engine)
print(dir(car1))
print(len(dir(car1)))'''
# Constructor Pattern:-
# Methods:-
class Car:
    # Constructor
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine

    def self_engine(self):
        print(f"The car has {self.engine} engine")

    def engine2(self,engine):
        print(f"The car has {engine} engine")

    def car_paint(self,paint):
        print(f"The car is of {paint} colour")
car1=Car(4,4,"Petrol")

car1.self_engine()

car1.engine2("Diesel")

car1.car_paint("Red")

'''print(f"The no.of tyres in car1 is {car1.tyres}")
print("The no.of windows in car1 is {}".format(car1.windows))
print(f"car1 has {car1.engine} engine")'''