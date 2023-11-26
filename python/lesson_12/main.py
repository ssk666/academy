# import re
# data = {'2023': 0, '2023/01': 100, '2022/02': 0}
# # можно внести в список сразу все месяца, чтобы программа работала быстрее, тк она ищет месяц за одну операцию
# #а если в год вложен словарь из месяцев, то уже 2 операции, тк проваливаемся вниз
#
# def add_money() -> None:
#     date = input('гггг/мм: ')
#     if re.match(r'\d{4}/\d{2}', date):
#         money = float(input(f'Внесите прибыль за {date}: '))
#         year, month = date.split('/')
#         data.setdefault(year, 0)
#         data.setdefault(date, 0)
#         data[date] += money
#         data[year] += money
#     else:
#         print('Формат даты неверный')
#
# def get_month_profit() -> None:
#     date = input('гггг/мм: ')
#     if re.match(r'\d{4}/\d{2}', date):
#         if data in data.keys():
#             print(f'Ваша прибыль за {date} составила: {data[date]}')
#         else:
#             print('Такого месяца - нет')
#     else:
#         print('Неверный формат даты')
#
# def get_year_profit() -> None:
#     year = input('Введите год: ')
#     if re.match(r'\d{4}', year) and year in data.keys():
#         print(f'Ваша прибыль за {year} равна {data[year]}')
#     else:
#         print('Такого года - нет!')
#
#
# def main() -> None:
#     while True:
#         choice = input('1 - Внести прибыль за период в формате гггг/мм: \n'
#                        '2 - Получить прибыль за конкретный месяц гггг/мм: \n'
#                        '3 - Получить прибыль за конкретный год гггг: \n'
#                        'Ввод: ')
#         if choice == '1':
#             add_money()
#         elif choice == '2':
#             get_month_profit()
#         elif choice == '3':
#             get_year_profit()
#         else:
#             print('Такой команды - нет')
#
# main()



# Задача
import re
contacts = {}

def add_contact() -> None:
    tel = input('Введи номер телефона: ')
    if re.match(r'\+7\d{10}', tel):
        name = input('Введите новый контакт: ')
        contacts.setdefault(tel, name)
    else:
        print('Что-то введено не так')

def delete_contact() -> None:
    wat_del = input('Введите номер: ')
    if wat_del in contacts:
        contacts.pop(wat_del)
        print('success')
    else:
        print('Такого номера нет')

def show_contacts():
    # print(f'{contacts}')
    print(**contacts)

def edit_contact() -> None:
    wat_edit = input('Введите контакт (номер телефона): ')
    if wat_edit in contacts:
        print(contacts[wat_edit])
        x = input('Что хотите изменить: ')
        if x == 'телефон':
            contacts.update(x)

def main() -> None:
    while True:
        choice = input('1 - Добавить контакт: \n'
                       '2 - Удалить контакт: \n'
                       '3 - Показать контакты: \n'
                       '4 - Изменить контакт: \n'
                       'Ввод: ')
        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            show_contacts()
        elif choice == '4':
            edit_contact()
        else:
            print('Такой команды - нет')


main()



# Синтаксический сахар

# def info_man(name, age):
#     print(name, age)
#
#
# data = {'name': 'Ivan', 'age': 22}
#
# info_man(**data)
# # убирает скобки и кавычки и выдает в чистом виде

# def info_man_2(name, age):
#     print(name, age)
#
# list_info = ['Marat', 21]
#
# info_man_2(*list_info)
# распаковка списка через одну звездочку *


# names_list = ['Marat', 'Stepka', 'Said', 'Tema']
#
# names_dict = {i + 1: names_list[i] for i in range(len(names_list))}
# names_dict = {i: [j for j in i] for i in names_list}
#
# print(names_dict)















