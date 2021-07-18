cost = int(input('Стоимость квартиры? '))
square = int(input('Площадь квартиры? '))
if cost <= 10 and square >= 100 or cost <= 7 and square >= 80:
    print('Подходит!')
else:
    print('Не Подходит!')
