num = int(input('Введите число в билете: '))
num1 = num // 1000
num2 = num % 1000
if num1 == num2:
    print('Этот билет счастливый! ', num)
else:
    print('Этот билет не счастливый!')
