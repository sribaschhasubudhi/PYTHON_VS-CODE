# Write a Python program that creates an Order class with a total amount, 
# then creates a DiscountedOrder subclass that applies a 10% discount to the total.

class Order:
    def __init__(self):
        self.amount=100

class DiscountOrder(Order):
    def __init__(self):
        super().__init__()

    def discount(self):
        self.amount-=(0.1*self.amount)
        print(f"Discounted Price: ₹{self.amount}")

dis=DiscountOrder()
dis.discount()
