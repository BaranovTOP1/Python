one = int(input('Введите отработанные часы: '))
two = int(input('Введите остаток по кредиту: '))
three = int(input('Введите траты на еду: '))
eatkredit = two + three
work = 200 * one / 2 ** 3 + one
if work >= eatkredit:
    print('Часов хватает. Можно отдохнуть!')
else:
    print('Часов не хватает. Придётся работать!')
