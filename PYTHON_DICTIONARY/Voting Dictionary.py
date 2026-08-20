votes={1:'a',2:'b',3:'c',4:'a',5:'a',6:'b'}
a=b=c=0
for i in votes:
    if votes[i]=='a':
        a+=1
    elif votes[i]=='b':
        b+=1
    elif votes[i]=='c':
        c+=1
if a>b and a>c:
    print("a is the winner")
elif b>a and b>c:
    print("b is the winner")
elif c>a and c>b:
    print("c is the winner")
else:
    print("voting sessions are nullified. Martial law has been imposed.")
