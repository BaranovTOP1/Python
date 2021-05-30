minutes=int(input('Введите количество минут : '))
hour = minutes//60
remaining = minutes-hour*60
print('часов ', hour, ', минут ', remaining)