# Write a Python program to sort a list of tuples using Lambda.
exam=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sorted(exam))
print(sorted(exam,key=lambda x:x[1]))