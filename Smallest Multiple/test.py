import math


done = False
x = 20
k = 2

while(done == False):
    while(k <= 20):
        if (x % k != 0):
            break
        elif(x % k == 0 and k == 20):
            done = True
            print("This is it:" + str(x))
        k = k + 1
    k = 2
    x = x + 20
