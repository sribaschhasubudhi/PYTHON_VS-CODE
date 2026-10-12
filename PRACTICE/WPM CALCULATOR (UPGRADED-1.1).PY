'''This is the upgraded version of the WPM CALCULATOR. The first version couldn't calculate
    a large text; if provided at a time. This calculator is made to solve that problem.'''

'''In this program, you need to provide your written text in  3 separate parts, one by one.
    the calculator counts the length of the part and sums it up, dividing it later by 5 to
    calculate the total words present in the text and then divides it by the time provided
    to calculate the standard wpm.'''

chars=0
for i in range (3):
    text=input("Enter the text:- ")
    print(" ")
    chars+=len(text)
words=chars/5
time=int(input("Enter the time (in minutes):- "))
wpm=round(words/time,2)
print(f"Your speed is {wpm} words per minute")