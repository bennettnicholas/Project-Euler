import math
List = []
num = 100001

def palindrome (num):
    total = num
    minus = total

    if num < 10:
        List.append(num)
    else:
        palindrome(num // 10)
        List.append(num % 10)


palindrome(num)

print List
length = len(List)
j = length - 1
x = 0

if length % 2 == 0:
    while (x < length / 2):
        if (List[x] != List[j]):
            break
        elif((x + 1) == (length / 2)):
            print num

        x = x + 1
        j = j - 1
