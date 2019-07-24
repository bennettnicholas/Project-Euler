import math

primes = [2]
isprime = True
count = 1
x = 2
highest = 0

while (x < 600851475143) :
    for y in primes:
        if(x%y == 0):
            isprime = False
            break
    if(isprime == True):
        primes.append(x)
        count = count + 1
    if(count == 10001 and isprime == True):
        print x
        break
    isprime = True
    x = x + 1