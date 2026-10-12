# Write a Python program to check whether a given string is a number or not using Lambda.
only_numbers=[2,4,49,"Hello",18,"world"]

# Normal Method:-
checkint=lambda num:type(num)==int
for i in only_numbers:
    print(f"{i} is {checkint(i)}")

# Lambda Function (Method-1):-
result=list(map(lambda x:type(x)==int,only_numbers))
print(result)

# Lambda Function (Method-2):-
check=list(map(lambda x:isinstance(x,int),only_numbers))
print(check)