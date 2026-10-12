# Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
copies=['bcda', 'abce', 'cbda', 'cbea', 'adcb']
check="abcd"

# Normal Method:-
anagrams=[]
for word in copies:
    if sorted(word)==sorted(check):
        anagrams.append(word)
print(anagrams)

# Lambda Function Method:-
anagrams=list(filter(lambda x:sorted(x)==sorted(check),copies))
print(anagrams)