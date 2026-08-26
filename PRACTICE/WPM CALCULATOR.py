'''Standard WPM is calculated by dividing the sum of the characters present in the text, 
by 5 and  then dividing the value by number of minutes.'''

text=input("Enter the text:-")
time=int(input("Enter the time in minutes:-"))
characters=[]
for i in text:
    characters.append(i)
cal_words=len(characters)/5
wpm=round(cal_words/time,2)
print(f"Your speed is {wpm} words per minute")