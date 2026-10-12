# Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.
num_range=range(1,41)
string_num=[str(i) for i in num_range]

# Normal method:-
div_it=[]
for num in num_range:
    digits=str(num)
    if "0" in digits:
        continue
    elif all(num % int(i)==0 for i in digits):      # Most Important Step
        div_it.append(num)
print(div_it)

# Lambda Function Method-1:-
div_result=list(filter(lambda n:
                       all(int(d)!=0 and n%int(d)==0
                           for d in str(n)),num_range))
print(div_result)

# Lambda Function Method-2:-
it_result=list(filter(lambda s:
                      all(int(n)!=0 and int(s)%int(n)==0 
                          for n in s),string_num))
it_int=[int(s) for s in it_result]
print(it_int)