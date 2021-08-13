mon = 0
while True:
    num = int(input('Введите число: '))
    if num == 0:
        break
    if num % 2 == 0:
        mon += 1
print(mon)
