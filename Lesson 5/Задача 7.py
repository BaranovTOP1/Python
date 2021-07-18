num1 = int(input('Введите число: '))
num2 = int(input('Введите число: '))
num3 = int(input('Введите число: '))
if num1 == num2 == num3:
    print('Все три числа ровны!', num1)
elif (num1 == num2 != num3) or (num1 != num2 == num3) or (num1 == num3 != num2):
    print('Два числа ровны!')
else:
    print('Нет одинаковых чисел!')
