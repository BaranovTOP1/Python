cena = int(input('Введите стоимость первого товара: ')) + int(
    input('Введите стоимость второго товара: ')) + int(
    input('Введите стоимость третьего товара: '))

cena2 = cena + (cena * 10 / 100)
if cena <= 10000:
    print(cena)
else:
    print(cena2)
