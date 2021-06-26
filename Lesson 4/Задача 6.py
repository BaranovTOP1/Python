kostya = int(input('Кубик Кости: '))
vlad = int(input('Кубик владельца: '))
suma = kostya + vlad
if kostya >= vlad:
    print(suma)
    print('Костя платит!')
    print('Игра окончена.')
else:
    print(suma)
    print('Владелиц платит!')
    print('Игра окончена.')
