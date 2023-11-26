# Функция в функции

from typing import Callable
import time


# def timer(func: Callable, *args, **kwargs):
#     print('Запуск таймера')
#     start = time.time()
#     res = func(*args, **kwargs)
#     print(f'Выполнение заняло {time.time() - start}')
#     return res


# def wrapper (функция обёртки)
#
# def timer(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs): # функция обёртка
#         start = time.time() # код для дополнения функционала
#         func(*args, **kwargs) # вызов функции
#         print(f'Функция {func.__name__}{func.__doc__} выполнялась за {time.time() - start}') # код для дополнения функционала
#     return wrapper # всегда должна возвращаться функция обертка
#
#
# @timer # прописали декоратор
# def square_sum(num):
#     """
#     Квадраты чисел
#     :param num:
#     :return:
#     """
#     nums = [i ** 2 for i in range(num)]
#     return nums
#
#
# @timer # прописали декоратор
# def cubes_sum():
#     nums = [i ** 3 for i in range(1000000)]
#     return nums
#
#
#
# square_sum(1011010)
# cubes_sum()


# def get_or_post(method):
#     def wrapper_func(func):
#         def wrapper():
#             res = func()
#             print(f'Запрос с методом {method} на ресурс {res} выполнен')
#         return wrapper
#     return wrapper_func
#
#
# @get_or_post('POST')
# def request():
#     url = 'http://test.com'
#     params = 'ru'
#     request_body = {}
#     return url, params, request_body
#
# request()




# def beauty_output(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         for i in result:
#             print(f'|{i}|')
#     return wrapper
#
#
#
# @beauty_output
# def names_output(names):
#     return names
#
#
# names_output(['Marat', 'Stepa', 'Tema'])



# import datetime
#
#
# def logging(func: Callable) -> Callable:
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#             print(f'{func.__name__}{func.__doc__}')
#         except BaseException as error:
#             with open('function_errors.log', 'a') as file:
#                 file.write(f'{func.__name__} | {datetime.datetime.now} | {error}\n')
#     return wrapper
#
#
# import functools
#
#
# def timer(func: Callable, *args, **kwargs):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Запуск таймера')
#         start = time.time()
#         res = func(*args, **kwargs)
#         print(f'Выполнение заняло {time.time() - start}')
#     return wrapper
#
#
# @timer
# @logging
# def concatenate(a, b):
#     return a + b
#
#
# @timer
# @logging
# def division(a, b):
#     return a / b
#
#
# concatenate(1, 'a')
# division(5, 0)





# Написать декоратор, который вызывает функцию 2 раза

#
# def pasta(func: Callable) -> Callable:
#     def wrapper (*args, **kwargs):
#         res_1 = func(*args, **kwargs)
#         res_2 = func(*args, **kwargs)
#         print(res_1, res_2)
#     return wrapper
#
#
# @pasta(5)
# def summ(a, b):
#
#     return a + b
#
#
# summ(1, 2)




# Вызов числа сколько-то раз через декоратор


# def multi(repeats):
#     def multi_func(func):
#         def wrapper(*args, **kwargs):
#             for i in range(repeats):
#                 res = func(*args, **kwargs)
#                 print(res)
#         return wrapper
#     return multi_func
#
#
# @multi(5)
# def nums(a, b):
#     return a + b
#
#
# nums(1, 2)


# Задержка программы

# import time
#
# def slow(sec) -> Callable:
#     def slow_func(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(sec)
#             res = func(*args, **kwargs)
#             print(res)
#         return wrapper
#     return slow_func
#
#
# @slow(5)
# def summ(a, b):
#     return a + b
#
#
# summ(1, 2)



# Проверка на разрешение в доступе

# def permission(func):
#     def wrapper():
#         age = int(input('Age: '))
#         if age >= 18:
#             func()
#         else:
#             print('Denied')
#     return wrapper
#
#
# @permission
# def secret():
#     info = 'TOP-SECRET'
#     print(info)
#
# secret()

















