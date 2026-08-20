# I am taking here the example of a bank account to learn about encapsulation in OOPs.
# I have defined:-
#   1. phone number and security pin as private attributes under class BankAccount.
#   2. balance and rate of interest as protected attributes. 
#       balance comes under class AccountBalance while roi comes under inherited class Interest.
#   3. name as public attribute under class Display.

# All the codelines are commented. 
# To run the codes, remove the comments and their respected calling statements.

## Private Attribute:-
'''class BankAccount:
    def __init__(self,phoneno,secpin):
        self.__phoneno=phoneno
        self.__secpin=secpin

    def confidential(self):
        print(f"OTP has been sent to:{self.__phoneno}")
        print(f"THIS DATA IS CONFIDENTIAL:- Security Pin of Account No.0123XXXX4567 is {self.__secpin}")

account=BankAccount(9876543210,13579)'''
'''print(account.__phoneno)               # Shows AttributeError
print(account._BankAccount__phoneno)'''         # Name mangled

'''account._BankAccount__phoneno=7943575036
print(f"Phone number has been compromised. {account._BankAccount__phoneno} has access to your bank account.")
'''
''' ~> Even with name mangling, the information can be accessed and changed; which is wrong.
Hence, instead of printing the attribute, display the info by calling a method.'''
'''account.confidential()'''

## Protected Attribute:-
'''class AccountBalance:
    def __init__(self,balance):
        self._balance=balance

    def money(self):
        print(f"Your account balance:{self._balance:,} USD")'''

# Using Inheritance:-
'''class Interest(AccountBalance):
    def __init__(self,balance,roi):
        super().__init__(balance)
        self._roi=roi

    def display_roi(self):
        print(f"{self._roi}% interest has been applied on {self._balance}")'''

'''ewallet=AccountBalance(12045)
ewallet.money()
print(ewallet._balance)             # No name mangling'''

'''rate=Interest(ewallet._balance,4)
rate.display_roi()'''

## Public Attribute :-
'''class Display:
    def __init__(self,name):
        self.name=name
    def greetings(self):
        print(f"Namaste {self.name}; Welcome to eWallet")

you=Display("Sribaschha")
you.greetings()'''