import math

natural_num = 1
sumofsquares = 0
squareofsums = 0
diff = 0

while natural_num <= 100:
    sumofsquares = sumofsquares + (natural_num ** 2)
    natural_num = natural_num + 1

natural_num = 1

while natural_num <= 100:
    squareofsums = squareofsums + natural_num
    natural_num = natural_num + 1
squareofsums = squareofsums * squareofsums

diff = squareofsums - sumofsquares

print diff