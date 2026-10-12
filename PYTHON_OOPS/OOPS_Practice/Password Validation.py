# Write a Python program to create a User class that stores a username and a password. 
# Add a check_password(input_password) method that returns True if the input matches the stored password, and False otherwise.

class User:
    def __init__(self):
        self.__password="Feuttccine444"
    def check_password(self):
        input_password=input("Enter password:-")
        if input_password=="Feuttccine444":
            return True
        else:
            return F"{input_password} is wrong"

alfredo=User()
print(alfredo.check_password())