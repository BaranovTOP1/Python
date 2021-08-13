z_num = int(input('Загадайте число: '))
o_num = int(input('Отгадайте число: '))
count = 1
while z_num != o_num:
    o_num = int(input('Отгадайте число: '))
    if o_num < z_num:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif o_num > z_num:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    count += 1
    if z_num == o_num:
        print('Вы угадали! Число попыток:', count)
        break
