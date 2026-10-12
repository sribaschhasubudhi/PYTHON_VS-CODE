'''IMPORTANT AND SPECIAL'''
# Write a Python program that creates a Passenger class and a Flight class. 
# The Flight class should manage a list of Passenger objects and block further bookings when the seat capacity is reached.

class Passenger:
    # Constructor method:-
    def __init__(self):
        self.name=input("Enter your name:-")
        self.seats=int(input("Enter number of seats to be booked:-"))
        
class Flight():
    # Constructor method:-
    def __init__(self,vacant_seats):
        self.vacant_seats=int(vacant_seats)
        self.passengers=[]
        pass

    # Checking vacant seats:-
    def vacancy(self):
        passenger=Passenger()                       # Flight HAS Passengers
        # This is not inheritance, this is composition.

        if passenger.seats<=self.vacant_seats:
            self.passengers.append(passenger.name)
            self.vacant_seats=self.vacant_seats - passenger.seats
            print(f"{self.vacant_seats} seats are available")

        elif self.vacant_seats==0:
            print(f"No seats available. All seats are booked")

        else:
            print(f"Can not book {passenger.seats}")
            print(f"Only {self.vacant_seats} available")

    def display_list(self):
        print(f"Passengers name list:-{self.passengers}")
            

sa458=Flight(10)
sa458.vacancy()      # person-1
sa458.vacancy()      # person-2
sa458.vacancy()      # person-3
sa458.display_list() # Name of all the passengers on board