kostya = int(input('Кубик Кости: '))
vlad = int(input('Кубик владельца: '))
suma = kostya + vlad
suma1 = kostya - vlad
if kostya >= vlad:
    print(suma1)
    print('Костя платит!')
    print('Игра окончена.')
else:
    print(suma)
    print('Владелиц платит!')
    print('Игра окончена.')
