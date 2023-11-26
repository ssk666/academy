# tuple_1 = ('Ivan', 15) #можно получать по индексу
# print(tuple_1[0])
# print(tuple_1 + ('Petr', 12)) #добавить
# print(tuple_1 * 2) #умножить
#
# tuple_2 = ('Mara', 21)
# print(tuple_2.count(21))
# print(tuple_2.index(21))



# tuple_1 = ('Mara', 17) # 56 байт # O(n)
# list_1 = ['Mara', 17] # 72 байта # 0(n)
# dict_1 = {'Mara': 17} # 232 байта # O(1)


# dict_1 = {('Marat', 'Maratov'): 21} # засунули кортеж в словарь
# print(dict_1[('Marat', 'Maratov')]) # вызываем по ключу, получаем = 21


# list_1 = ['Marat', 'Gabitov']
# tuple_1 = ('Marat', 'Gabitov')
# print(tuple(list_1)) # преобразуется спокойно в кортеж
# print(list(tuple_1)) # преобразуется спокойно в список



# zip

# list_1 = ['London', 'Manchester']
# list_2 = [100, 200]
# print(dict(zip(list_1, list_2)))
# {'London': 100, 'Manchester': 200} - соотносит пары по индексу (если будет чего-то больше, то он просто не учтет)
# с кортежами тоже будет работать

# list_1 = ['London', 'Manchester']
# list_2 = (100, 200)
# print(tuple(zip(list_1, list_2)))
# (('London', 100), ('Manchester', 200))


# import re
# dictionary = {}
#
# def add_competition() -> None:
#     comp = input('Введите дисциплину: ')
#     date = input('Введите дату проведения и время dd/mm/yyyy hh:mm: ')
#     if re.match(r'\d\d/\d\d/\d{4} \d\d:\d\d', date) and (comp, date) not in dictionary:
#         dictionary.update({(comp, date): []})
#         print('Соревнование добавлено!')
#         return
#     print('Ошибка') #не прописываем else: тк прописали return
#
#
# def add_members() -> None:
#     comp = input('Введите дисциплину: ')
#     date = input('Введите дату проведения и время dd/mm/yyyy hh:mm: ')
#     if re.match(r'\d\d/\d\d/\d{4} \d\d:\d\d', date) and (comp, date) in dictionary:
#         choice = input('Добавить участника(add) / Исключить участника(del): ')
#         member = dictionary[(comp, date)]
#         if choice == 'add':
#             enter_memb = input('Введите участника через запятую: ').split(', ')
#             dictionary[(comp, date)] = member + enter_memb
#             print('Участники добавлены')
#         elif choice == 'del':
#             del_memb = input('Введите участника через запятую: ').split(', ')
#             for i in del_memb:
#                 member.remove(i)
#             dictionary[(comp, date)] = member
#             print('Участники удалены')
#             return
#         else:
#             print('Ошибка ввода')
#
#
# def show_info() -> None:
#     comp = input('Введите дисциплину: ')
#     date = input('Введите дату проведения и время dd/mm/yyyy hh:mm: ')
#     if re.match(r'\d\d/\d\d/\d{4} \d\d:\d\d', date) and (comp, date) in dictionary:
#         print(f'{comp} {date}')
#         for index, i in enumerate(dictionary[(comp, date)]):
#             print(f'{index + 1} {i}')
#         return
#     print('Ошибка')
#
# def main() -> None:
#     while True:
#         choice = input('1-Добавить соревнование\n'
#                        '2-Внести участников\n'
#                        '3-Показать график по соревнованию\n'
#                        'Enter: ')
#         if choice == '1':
#             add_competition()
#         elif choice == '2':
#             add_members()
#         elif choice == '3':
#             show_info()
#
#
# main()




# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
# def caesar(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ')for sym in text.lower()]
#     return ''.join(decrypted_list)
#
# text = input('Введите текст: ')
# shift = int(input('Введите сдвиг: '))
#
#
# print(caesar(text,shift))



# site = {
#     'body': {
#         'div': {
#             'ul': {
#                 'li_1': {},
#                 'li_2': {
#                     'a': {
#                         'href': 'ссылка'
#                     }
#                 }
#             }
#         }
#     }
# }
#
# def get(key, dictionary, level=0):
#     if key in dictionary.keys():
#         print(dictionary[key])
#         print(level)
#         return
#     for value in dictionary.keys():
#         if isinstance(dictionary[value], dict):
#             get(key, dictionary[value], level + 1)
#
#
# print(get('href', site))



# Задание 2

# fruit_tuple = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
# fruit = input(': ')
# count = 0
#
# for i_fruit in fruit_tuple:
#     if fruit in i_fruit:
#         count += 1
# print(count)


