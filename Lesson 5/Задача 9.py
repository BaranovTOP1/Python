income = int(input('Введите Ваш доход: '))
nal = 0
if income > 50000:
    nal = (income - 50000) * 0.3
    income = 50000
if 50000 >= income > 10000:
    nal += (income - 10000) * 0.2
    income = 10000
nal += 0.13 * income
print('Ваш налог: ', nal)
