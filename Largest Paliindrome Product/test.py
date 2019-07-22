import math

def palindrome (ii, kk, huge):
    big = huge
    total = ii * kk
    minus = total

    hunthou = total / 100000
    minus = minus - (hunthou * 100000)
    tenthou = minus / 10000
    minus = minus - (tenthou * 10000)
    thou = minus / 1000
    minus = minus - (thou * 1000)
    hun = minus / 100
    minus = minus - (hun * 100)
    ten = minus / 10
    minus = minus - (ten * 10)
    one = minus

    if (hunthou == one and tenthou == ten and thou == hun and total > big):
        big = total
    return big



ii = 999
kk = 999
done = False
largest = 0

while(ii <= 999 and ii >= 100 and done == False):

    while(kk <= 999 and kk >= 100 and done == False):
	   largest = palindrome(ii, kk, largest)
	   kk = kk - 1
    kk = 999
    ii = ii - 1

print largest
