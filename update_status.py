result = []
while True:
    status = input('Введите статус ("выполнено", "в процессе", "отложено"): ')
    if status not in ["выполнено", "в процессе", "отложено"]:
        print('Неверный статус \U0001F643')
    else:
        result.append(status)