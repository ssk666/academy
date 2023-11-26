
# def function_1(a, b, *args): # *args - неименованные аргументы (их можно передавать хоть сколько)
#     print(a, b, args)
#
#
# function_1(1, 2, 3, 4, 5, 6)



# def summa(*args):
    # 1 способ
    # count = 0
    # for i_arg in args:
    #     count += i_arg
    #     # print(i_arg)
    # return count

    # 2 способ
#     return sum(args)
#
#
# print(summa(1, 3, 6, 9, 4, 22))



# def get_form(**kwargs): # аргументы по ключу
#     # print(kwargs)
#     print(kwargs['name']) # по ключу выводим
#
# get_form(name='Ivanov', email='ivanov@mail.ru') # ключ = 'значение'



# import requests
# def get(request, *args, **kwargs):
#     print(f'Сделан запрос на {request}')
#     print(f'Параметры запроса {kwargs["cache_control"]}')
#     print(f'Относительный путь {args[0]}')
#
#
# get('http://test.ru', '/page_1', cache_control='no-cache', content_type='hgrf')



# def function(group, degree, final_y, *args):
#     print(f'Группа: {group},\n'
#           f'Учёная степень: {degree}\n'
#           f'Год выпуска: {final_y}')
#
#     count = 0
#     for i_st in args:
#         count += 1
#         print(count, i_st)
#
# function('303', 'mag', 2020, 'Мара Габит', 'Падурин Степан')


# переделать по фото Мары в вк
# def data(**kwargs):
#     try:
#         if kwargs['tel'] is None and ['email'] is None:
#             print('Переделывай')
#         print(kwargs)
#     except KeyError:
#         print('Переделать')
#
#     print(kwargs)
#
# data(email='mara2012@mail.ru', tel='48964',  surname='Gabitov')



# Анонимная функция

# square = lambda x: x ** 2
# # переменная = анонимная функция х(параметр): что выполняем
# print(square(5))

# square = lambda x, y: x ** y # добавили второй параметр
# print(square(5, 2))



nums_list = [1, 2, 3, 4, 5, 6, 7, 8]

#list
# square_nums_list = [i ** 2 for i in nums_list]
# print(square_nums_list)


# с каждой строчки ; в 3 раза оптимизированнее по весу
# square_nums_list_2 = map(lambda x: x ** 2, nums_list)
# for i in square_nums_list_2:
#     print(i)


# filtered_list = list(filter(lambda x: x > 4, nums_list))
# print(filtered_list)


# names_list = ['Ivan', 'Petya', 'Irina']
#
# filtered_list = list(filter(lambda x: x[0].lower() == 'i' and len(x) <= 4, names_list))
# print(filtered_list)


# nums = [123, 14575, 35, 8, 147, 489]

# filtered_nums = list(filter(lambda x: len(str(x)) == 3, nums)) # через filter
# filtered_nums = list(map(int, (filter(lambda x: len(x) == 3, map(str, nums))))) # через map

# print(filtered_nums)


students = [['Student 1', 4.1],
            ['Student 2', 3.5],
            ['Student 3', 4.],
            ['Student 4', 4.2],
            ['Student 5', 4.2],
            ['Student 6', 5.0],
            ['Student 7', 4.9]
            ]

sorted_list = sorted(students, key=lambda x: x[1])
sorted_list_2 = sorted(students, key=lambda x: int(x[0].split()[1]))
print(sorted_list_2)

































































































