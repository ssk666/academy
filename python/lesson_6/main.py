# import sys

# my_list = ['Moscow', 'Ekb', 'Saint-P', 'Vorcuta', ] #пустой список
# my_list_2 = list(('Moscow', 'Ekb', 'Saint-P', 'Vorcuta')) # - второй способ вызвать список
# можно сделать список внутри списка, тогда список уменьшится в размере
# второй варинт списка занимает меньше памяти

# print(my_list)
# print(my_list_2)

# my_list.append('Asbest') # добавить что-то в конец списка
# my_list.remove('Asbest') # удалить что-то из списка
# deleted_city = my_list.pop() #сохраняет в переменную последний удаленный элемент списка
# my_list.pop(2) # удаляет по индексу
# my_list.insert(0, 'Rudniy') # - добавит значение по заданному индексу
# print(my_list.index('Ekb')) #- на каком месте по индексу стоит Екб (если есть дубликат, то найдет первый найденный)
# print(my_list.count('Rudniy')) # сколько в списке таких значений
# my_list[2] = 'London' # заменить второй город по индексу на значение
# print(my_list.reverse()) #справа налево выдает список



# my_list_3 = ['Ekb', 'Vorcuta', 'London', 'Washington', 'Moscow']

# for i_city in  my_list_3:
#     print(f'Город: {i_city}')

# for index in range(len(my_list_3)):
#     print(f'{index + 1} City: {my_list_3[index]}')



# Тестовое задание
# start = int(input('Введи начало: '))
# stop = int(input('Введи конец: '))
# user_list = []
#
# for i in range (start, stop + 1):
#     if i % 2 != 0:
#         user_list.append(i)
# print(user_list)


# Жеребьевочка
# basket_1 = ['Bayern', 'MU', 'Juventus', 'Barcelona']
# basket_2 = ['Real Madrid', 'PSG', 'Man City', 'Napoli']
#
# group_list = []
#
# for index in range(len(basket_1)):
#     if index % 2 != 0:
#         print(f'{basket_1[index]} VS {basket_2[index - 1]}')
#         print(f'{basket_1[index - 1]} VS {basket_2[index]}')



# numbers = [11, 2, 6, 12, 4, 10, 9, 81]
# numbers.sort() #- отсортировать по возрастанию
# numbers.sort(reverse=True) #- отсортировать по убыванию
# numbers_sorted = sorted(numbers) # то же самое, но создается копия; в памяти по индексу лежат по-разному
# print(numbers)



# string = 'hello python java ruby'
# print(string.split('*'))




# numbers = input('Введите числа через пробел: ').split()

# for i_num in numbers:
#     numbers[numbers.index(i_num)] = int(i_num) #взяли через индекс все числа и переформатировали в int


# for index, value in enumerate(numbers):
#     numbers[index] = int(value)
# print(numbers)


# numbers_int = list(map(int, numbers)) #map применяет к каждому значению int
# print(numbers_int)



# Мини-приложение

# films = ['Форсаж 5', 'Стажёр', 'Барби', 'Перевозчик', 'Челюсти', 'Наруто', ]
#
# liked_films = []
#
# while True:
#     choice = input('1 - Посмотреть список фильмов\n'
#                    '2 - Добавить фильм в избранное\n'
#                    '3 - Удалить фильм из избранного\n'
#                    'Выбрать: ')
#     if choice == '1':
#         print(f'Список фильмов: ', *films)
#     elif choice == '2':
#         film = input('Введите название фильма: ')
#         if film in films:
#             if film not in liked_films:
#                 liked_films.append(film)
#                 print('Успешно добавлен!')
#             else:
#                 print ('Такой фильм уже есть.')
#         else:
#             print('Такого фильма в нашей библиотеке нет и не будет')
#     if choice == '3':
#         film = input('Введите название фильма, который хотите удалить: ')
#         if film in liked_films:
#             liked_films.remove(film)
#         else:
#             print('Такого фильма у нас нет')
#     else:
#         print('exit')



# numbers = [1, 31, 4, -1, 313, 15, 7]
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))



# Задание 2
# numbers = input('Введи ряд чисел через пробел: ').split()
# f_num = input('Число: ')
#
# print(numbers.count((f_num)))



# Задание 3
# numbers = input('Введи ряд чисел: ').split()
#
# numbers = list(map(int, numbers))
# print(sum(numbers))
#
# count = 0
# for i in range(len(numbers)):
#     count += 1
# print(sum(numbers) / count)



# Задание 1
text = 'привет. как дела. чем занят. я изучаю питон. идем гулять.'


























