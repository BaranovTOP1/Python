good_esl = 0
bad_esl = 0
n = -1
while n != 0:
    n = int(input('Введите число: '))
    if n > 0:
        good_esl += 1
    if n < 0:
        bad_esl += 1
print('Количество положительных чисел: ', good_esl)
print('Количество отрицательных чисел: ', bad_esl)
