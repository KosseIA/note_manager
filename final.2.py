from datetime import datetime

username = input('Введите ваше имя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите содержание заметки: ')
status = input('Введите статус заметки (низкий, средний, высокий): ')
created_date = '-'.join(str(datetime.now().date()).split('-')[::-1])
issue_date = input('Введите дату дедлайна (в формате ДД-ММ-ГГГГ): ')
titles = []
for i in range(3):
    title = input('Введите заголовок заметки: ')
    titles.append(title)
print(titles)
print('Имя пользователя: ', username)
print('Заголовок заметки: ', title)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания: ', created_date)
print('Дата дедлайна: ', issue_date)
note = {
    'Имя пользователя': username,
    'Содержание заметки': content,
    'Статус': status,
    'Дата создания': created_date,
    'Дата изменения': issue_date,
    'Заголовок': title
}
print(note)
