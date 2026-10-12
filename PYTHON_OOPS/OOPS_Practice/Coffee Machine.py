# Write a Python program to create a CoffeeMachine class that tracks three resource attributes: water, coffee, and milk (in ml/g). 
# Add a make_latte() method that checks whether sufficient resources are available, deducts them if so, and prints an appropriate message in either case.

# Required:-
#  300 ml (1.25 cups) of fresh milk
#  30 ml water
#  7 grams coffee

class CoffeeMachine:
    def __init__(self,coffee,water,milk):
        self.coffee=coffee
        self.water=water
        self.milk=milk

    def make_latte(self):
        coffee=int(input("Enter the amount of coffee in grams:-"))
        water=int(input("Enter the amount of water in ml:-"))
        milk=int(input("Enter the amount of milk in ml:-"))

        if coffee==self.coffee and water==self.water and milk==self.milk:
            print(f"You have all the ingredients with perfect measurements.")
            print(f"You can now make a perfect latte.")

        else:
            print(f"Your measurements are wrong. You will ruin it")
            print(f"This is the worst latte!")
            print(f"Not even a dog will have it. GET LOST!")

chef=CoffeeMachine(7,30,300)
chef.make_latte()