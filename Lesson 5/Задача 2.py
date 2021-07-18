one = int(input('Введите первое число: '))
two = int(input('Введите второе число: '))
three = int(input('Введите третье число: '))
if one > two:
    if one > three:
        print(one)
    else:
        print(three)
else:
    if two > three:
        print(two)
    else:
        print(three)
