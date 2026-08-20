# Write a Python program to create a Product class with three instance attributes: name, price, and quantity. 
# Add a method total_value() that returns the total stock value by multiplying price by quantity.

class Product:
    def __init__(self):
        self.name=input("Enter the name of the product:-")
        self.price=int(input("Enter the price of the product:-"))
        self.quantity=int(input("Enter the quantity of the product:-"))

    def total_value(self):
        stock_value=self.price*self.quantity
        return stock_value

book=Product()
print(book.total_value())