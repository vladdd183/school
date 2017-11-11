a = int(input('Days: '))
temp = []
summa = 0
k = 0
for x in range(1, a + 1):
    temp.append(input(str(x) + ' day: '))
for x in range(0, len(temp)):
    if int(temp[x]) > 0:
        summa += int(temp[x])
        k += 1
print(summa/k)
