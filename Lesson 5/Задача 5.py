rating = int(input('Что получил по математике? '))
if rating <= 3:
    print('Плохо. Марш учиться!')
elif rating >= 4 and rating <= 5:
    print('Молодец! Можешь отдохнуть.')
else:
    print('Вы ввели неверную оценку!')
