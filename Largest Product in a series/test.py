largest = 0
value = 1
count = 0
x = 0
f = open("series.txt", "r")
if f.mode == 'r':
    contents = f.read()
    while(x < 1000):
        print str(value) + " * " + str(ord(contents[x])-48)
        value = long(value) * (ord(contents[x]) - 48)
        print "Final " + str(value)
        if(count == 12):
            x = x - 12
            print "END OF STRING LENGTH"
            if(value > largest):
                largest = value
            value = 1
        x = x + 1
        count = count + 1
        if(count ==13):
            count = 0
    print str(largest)

