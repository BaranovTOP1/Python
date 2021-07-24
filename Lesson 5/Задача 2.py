one = int(input('Введите первое число: '))
two = int(input('Введите второе число: '))
three = int(input('Введите третье число: '))
if one > two and one > three:
    print(one)
elif two > one and two > three:
    print(two)
else:
    print(three)
