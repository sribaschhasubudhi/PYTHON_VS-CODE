# Generate a list of prime numbers from 1 to 100
prime=[]
for i in range(2,101):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break           # Breaks the 2nd for loop

    if is_prime:            # Same as if is_prime==True:
        prime.append(i)
print(prime)