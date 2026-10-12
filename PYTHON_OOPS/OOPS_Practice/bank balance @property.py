# Write a Python program that creates a BankAccount class where the balance is stored as a private attribute __balance, and
# exposed safely through a @property getter and a setter that validates the value before updating it.

class BankAccount:
    # constructor method:-
    def __init__(self):
        self.__balance=1000
        

    # @property method:- 
    @property       
    def update_account(self):
        return f"Your account balance is ₹{self.__balance}"

    # @update_account.setter method:-
    @update_account.setter
    def update_account(self,withdrawal):
        withdrawal=int(input("Enter the amount to withdraw:-"))
        if withdrawal<=self.__balance:
            self.__balance-=withdrawal
            print(f"You have deposited ₹{withdrawal} into your account")
            print(f"Your account balance is ₹{self.__balance}")
        else:
            print("You can't withdraw. It will make the balance negative")

    def deposit_to_account(self):
        deposit=int(input("Enter the amount to deposit:-"))
        self.__balance+=deposit
        print(f"You have deposited ₹{deposit} into your account")
        print(f"Your account balance is ₹{self.__balance}")
        

holder1=BankAccount()
holder1.deposit_to_account()
holder1.update_account
holder1.update_account=200