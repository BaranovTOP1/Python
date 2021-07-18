num = int(input('Введите число: '))
if (num < -9 and num > -100) or (num > 9 and num < 100):
    print('Это двузначное число!')
else:
    print('Это не двузначное число!')
