import datetime

created_date = '-'.join(str(datetime.datetime.now().date()).split('-')[::-1])
print('Текущая дата:', created_date)
user_date = input('Введите дату дедлайна (в формате день-месяц-год): ')
# Проверяем ввод даты в нужном формате
try:
    d1, m1, y1 = list(map(int, created_date.split('-')))
    d2, m2, y2 = list(map(int, user_date.split('-')))
except ValueError:
    print("Необходимо вводить дату в формате дд-мм-гггг!")
else:
    # Проверяем адекватность формата даты
    try:
        gap = (datetime.datetime(y1, m1, d1) - datetime.datetime(y2, m2, d2)).days
    except ValueError:
        print("Введите верный формат даты!")
    else:
        if gap > 0:
            print(f'Внимание! Дедлайн истёк {gap} дня назад.')
        elif gap == 0:
            print('Дедлайн сегодня!')
        else:
            print(f'До дедлайна осталось {abs(gap)} дня.')
