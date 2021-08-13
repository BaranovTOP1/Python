hou = 0
print('Начался 8-часовой рабочий день')
tasks = 0
call_wife = False
while hou < 8:
    hou += 1
    print(hou, '- й час')
    tasks += int(input('Сколько задач решил Максим? '))
    wife_call = int(input('Звонит жена. Взять трубку? 1 — да, 0 — нет '))
    if wife_call == 1 and call_wife == True:
        print('Нужно зайти в магазин.')
print('Рабочий день закончился. Всего выполнено задач: ', tasks)
