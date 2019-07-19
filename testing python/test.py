import math

primes = [2]
isprime = False
x = 2
highest = 0

while x < 600851475143:

    for y in primes:
        if(x%y == 0):
            break
        elif (x % y != 0):
            primes.append(x)

    x = x + 1
for z in primes:
    if(600851475143 % z == 0 and z > highest):
        highest = z
print highest
