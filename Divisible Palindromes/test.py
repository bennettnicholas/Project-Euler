import math
List = []
num = 10 ** 32

def list_fill (num):
    total = num
    minus = total

    if num < 10:
        List.append(num)
    else:
        list_fill(num // 10)
        List.append(num % 10)

def check_palindrome():

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

ii = num
while ii > 0:
    list_fill(ii)
    check_palindrome()
    ii = ii - 1
    if(ii % 50000000000000000 == 0):
        print ii


print List

