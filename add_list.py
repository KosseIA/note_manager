from datetime import datetime

now = datetime.now()
only_date = now.date()

username = input('Введите ваше имя: ')
title = input('Введите заголовок заметки: ')
title2 = input('Введите заголовок второй заметки: ')
title3 = input('Введие заголовок третьей заметки: ')
title4 = input('Введите заголовок четвертой заметки: ')
titles = [title2, title3, title4] # очень не уверена, что сделала правильно
content = input('Введите содержание заметки: ')
status = 'Выполнено!'
created_date = now
issue_date = input('Введите дату дедлайна: ')
print('Имя пользователя: ', username)
print('Заголовок заметки: ', title)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания: ', only_date)
print('Дата дедлайна: ',issue_date)
