x = int(input('Сумма вклада? '))
p = int(input('Введите % '))
y = int(input('Итоговая сумма? '))
res = 0
while x <= y:
    x = ((x + x * (p / 100)) // 1)
    res += 1
print(res)
