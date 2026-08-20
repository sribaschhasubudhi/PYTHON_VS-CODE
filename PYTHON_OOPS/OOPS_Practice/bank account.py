# Write a Python program to create a BankAccount class with a balance attribute and two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts funds but prevents the balance from going below zero.
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
        print(f"You have ₹{self.balance:,} in your Bank Account")

    def deposit(self):
        amount=int(input("Enter the amount to deposit:-"))
        self.balance+=amount
        print(f"₹{amount} credited to your bank account")
        print(f"New balance:- ₹{self.balance:,}")

    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:-"))
        if amount>self.balance:
            print(f"You can't withdraw ₹{amount:,} because it will make you bankrupt")
        else:
            self.balance-=amount
            print(f"₹{amount} debited from your bank account")
            print(f"New balance:- ₹{self.balance:,}")

holder=BankAccount(100000)
def signin():
    print(f"Do you want to withdraw or deposit money?")
    ask=input("Type W for withdraw and D for deposit. Type E to exit :-")

    if ask in {"w","W"}:
        holder.withdraw()

    elif ask in {"D","d"}:
        holder.deposit()

    elif ask in {"E","e"}:
        print(f"Thank You. You have successfully logged out")
        
signin()
