def factor(x):
    factors = []
    for i in range(1, x):
              if x % i == 0:
                   factors.append(i)
    return factors
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
i = 1
number = '110'
e = []
while i < 30:
    k = int(number, 2)
    #q = factor(k)
    #w = listsum(q)
    print(str(k) + ' : ' + number)
    #if k == w:
    #    e.append(k)

    number = '1' + number + '0'
    i = i + 1
print(e)
