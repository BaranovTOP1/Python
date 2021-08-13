summ = int(input('Введите число: '))
coun = 0
while summ > 0:
    coun += 1
    summ = summ // 10
print(coun)
