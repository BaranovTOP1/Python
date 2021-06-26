val = sum(map(int, list(input('Введите пробег: '))))
summ = int(input('Введите сегодняшнее число: '))
if val > summ:
    print('Сброс.')
    print('Пробег: ', val)
else:
    print('Сегодня не сломался.')
    print('Пробег: ', val)
