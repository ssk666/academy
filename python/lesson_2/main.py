# age = int(input('Введите Ваш возраст: '))
# if age >= 18 and age<= 70: - сократили (if 18 <= age <= 70:)
#     print('Вы можете зарегистрироваться')
# else:
#     print('Вам нельзя зарегистрироваться')

# weekday = int(input('Введите номер дня недели: '))
# if weekday == 1:
#     print('Понедельник')
# elif weekday == 2:
#     print('Вторник')
# elif weekday == 3:
#     print('Среда')
# elif weekday == 4:
#     print('Четверг')
# elif weekday == 5: - если пишем elif, то else срабатывает на все (elif = иначе если)
#     print('Пятница')
# elif weekday == 6:
#     print('Суббота')
# elif weekday == 7:
#     print('Воскресенье')
# else:
#     print('Введи число от 1 до 7')


# email = 'mara@dikiy.ru'
# password = 'zloy'
# auth = False - флаг
#
# email_input = input('Введите свою почту: ')
# password_input = input('Введите свой пароль: ')
#
# if email_input == email:
#     if password_input == password:
#         auth = True - проверяем флаг
#         print('Success')
#     else:
#         print('Decline password')
# else:
#     print('Decline email')
#
# # Для псевдоумников от 3.10py
# match(auth):
#     case True:
#         print('Успешная авторизация')
#     case False:
#         print('Не получилось авторизаваться')
#     case _:
#         print('Else')


# number = int(input('Введите число: '))
#
# if number % 2 == 0: #- кратно 2-ум
#     print('Even')
# else:
#     print('Odd')
#
# if number % 2 != 0: #- НЕ кратно 2-ум
#     print('Odd')
# else:
#     print('Even')


# from math import sqrt
# print('a*x^2 + b*x + c')
#
# a = float(input('Введите кофф а: '))
# b = float(input('Введите кофф b: '))
# c = float(input('Введите кофф c: '))
#
# D = b**2 - 4 * a * c
# if D < 0:
#     print('No roots')
# elif D== 0:
#     x = -b / (2 * a)
#     print(f'x = {x}')
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - D**0.5) / (2 * a)
#
#     print(f'x1={round(x1, 2)} x2={round (x2, 2)}')


# number_1 = int(input('1-e число: '))
# number_2 = int(input('2-e число: '))
#
# if number_2 == 0:
#     print('Нельзя делить так')
# else:
#     print(number_1/ number_2)


# number_1 = int(input('1-e число: '))
# number_2 = int(input('2-e число: '))
#
# try:
#     print(number_1 / number_2)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print('0 ошибок')
# finally:
#     print('FINALLY started')


# try:
#     raise ValueError('Ошибка вызвана специально')
# except FileNotFoundError:
#     print('Обработана ошибка')


# try:
#     raise ValueError
# except ValueError:
#     print('Обработчик ошибки ValueError 1')
# except BaseException:
#     print('Обработчик ошибки ValueError 2')


# try:
#     year = int(input('What is the year: '))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print ('Visokosniy bratka')
#     else:
#         print('Simple bratka')
# except (ValueError, TypeError):
#     print('It must be a number')


# Задача 2
# try:
#     number = int(input('Введи число: '))
#     if number % 7 == 0:
#         print('Number is multiply 7!')
#     else:
#         print('Number is not multiply 7(((')
# except (ValueError, TypeError):
#     print('It must be a number')


# Задача 3
# try:
#     number_1 = int(input('Enter the 1st num: '))
#     number_2 = int(input('Enter the 2nd num: '))
#     if number_1 > number_2:
#         print(number_1)
#     else:
#         print (number_2)
# except (ValueError):
#     print('It must be a num')


# Задача 4
# try:
#     number_1 = int(input('Enter the 1st num: '))
#     number_2 = int(input('Enter the 2nd num: '))
#     if number_1 < number_2:
#         print(f'{number_1}, {number_2}')
#     else:
#         print (f'{number_2}, {number_1}')
# except (ValueError):
#     print('It must be a num')


# Задача 5
# try:
#     number_1 = int(input('Enter the 1st num: '))
#     number_2 = int(input('Enter the 2nd num: '))
#     print('Choose an operation: \n 1 - sum\n 2 - difference\n 3 - average\n 4 - multiply\n')
#     x = int(input(''))
#     if x == 1:
#         print(number_1 + number_2)
#     elif x == 2:
#         print(number_1 - number_2)
#     elif x == 3:
#         print((number_1 + number_2) / 2)
#     elif x == 4:
#         print(number_1 * number_2)
#     else:
#         print('Try again')
# except (ValueError):
#     print('It must be a num')


# Задача 5
# sec = int(input('Введи время в секундах: '))
# print('Covert to: \n 1 - sec\n 2 - min\n 3 - hours\n do polunochi (00:00)')
# x = int(input(''))
# if x == 1:
#     print(43200 - sec)
# elif x == 2:
#     print((43200 - sec) / 60)
# elif x == 3:
#     t = (43200 - sec) / 3600
#     print(round(t, 2))
#
# else:
#     print('Try again')
















































