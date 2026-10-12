# Write a Python program to find the numbers in a given string and store them in a list. 
# Afterward, display the numbers that are longer than the length of the list in sorted form. 
line3="isdkfj dvdhvnhgeriugyer 43 ggt8ger geh 20 3 gr ege 7 14 bjdv dfvfgyuergh 45"
line3_lst=line3.split()

# => isdigit() returns True if the string contains only digits.
find_numbers=list(filter(lambda x:x.isdigit(),line3_lst))
print(find_numbers)
longer_numbers=list(filter(lambda y:int(y)>len(line3_lst),find_numbers))
print(sorted(longer_numbers))