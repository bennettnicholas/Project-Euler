import math

primes = [2]
isprime = True
x = 2
highest = 0

while (x < 600851475143) :
    if(600851475143 % x == 0):
        for y in primes:
            if(x%y == 0):
                isprime = False
                break
        if(isprime == True):
            primes.append(x)
            print x
        isprime = True
    else:
        pass

    x = x + 1

for z in primes:
    if(600851475143 % z == 0 and z > highest):
        highest = z
print highest
