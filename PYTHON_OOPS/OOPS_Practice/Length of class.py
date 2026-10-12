'''Important'''
# Write a Python program that creates a Cart class that stores a list of items, 
# and implements __len__ so that calling len(cart) returns the number of items currently in the cart.

class Cart:
    # Constructor Method:-
    def __init__(self):
        self.list=["steel","silver","copper","gold"]

    # Len Counting Method:-
    def __len__(self):
        return len(self.list)

metals=Cart()
print(f"The number of metal types present in the cart are {len(metals)}")
 # calling the object inside the len()