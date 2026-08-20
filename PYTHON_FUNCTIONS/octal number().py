def octal():

    octn=input("Enter octal number (without prefix):-")
    decn=int(octn,8)
    print("0o",octn,"in decimal number is",decn)
    binn=bin(decn)
    print("0o",octn,"in binary number is",binn)
    hexn=hex(decn)
    print("0o",octn,"in hexa-decimal number is",hexn)
octal()