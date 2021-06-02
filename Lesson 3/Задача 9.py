number = int(input("Введите число: "))
number1 = 0
while number > 0:
  digit = number % 10
  number = number // 10
  number1 = number1 * 10
  number1 = number1 + digit
  print('Перевернутое число:', number1)