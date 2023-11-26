#
# if __name__ == '__main__':
#     print('I am module')


# def summa(a, b, c):
#     return a + b + c
#
#
# print(summa(1, 775, 1))


# def print(string):
#     return
# нельзя называть функции зарезервированными именами

# value_1 = 10
#
# def my_function():
#     # global value_1
#     value = 0
#     print(value)
# локально пременную нельзя вызвать из функции, но глобальную функцию локально (внутри) можно

# my_function()
# print(value_1)


# val_1 = 1
#
# def func_1(a):
#     val_2 = 2
#     def func_2():
#         val_3 = 3
#         print(a)
#     print(val_2)
#     func_2()
#
# print(val_1)
# func_1(12)



# def check_is_happy_num(number: str) -> bool:  # (указали тип данных), -> какой тип данных возвращает
#     """
#     Проверяет является ли число счастливым
#     :param number: str
#     :return: bull
#     """
#     left = int(number[0]) + int(number[1]) + int(number[2])
#     right = int(number[3]) + int(number[4]) + int(number[5])
#     if left == right:
#         return True
#
#     return False
#
# print(check_is_happy_num('548632'))


#
# from typing import List
#
# def avg_age_of_people(people: List[list]) -> float:
#     """
#     Функция среднего возраста
#     :param people: List(list)
#     :return: float
#     """
#     average: int = sum([i_human[1] for i_human in people]) # используем генератор
#     return round(average / len(people), 1)
#
# people_list = [
#     ['Ivan', 35],
#     ['Mara', 27],
#     ['Stepa', 11],
# ]
#
# print(avg_age_of_people(people_list))



# Задание 2
# from typing import List
#
# def show_odd_nums(number1: int, number2: int) -> None:
#     """
#     Отображение всех нечет чисел в диапазоне
#     :param number1:
#     :param number2:
#     :return:
#     """
#
#
#     for i in range(number1, number2):
#         if i % 2 != 0:
#             print(i)
#
# number1 = 1
# number2 = 10

# print(show_odd_nums(number1,number2))



# Задание 3
# from typing import List
#
# def showing_direction_line(length: int, direction: int, symbol: str) -> bool:
#     """
#     Отображение линии в заданную сторону из символов с указанной длинной
#     vertical - True, horizontal - False
#     :param length: int
#     :param direction: str
#     :param symbol: str
#     :return: bool
#     """
#     # direction = int(input('1 - vert or 0 - hor: '))
#     # symbol = input('symbol: ')
#     # length = int(input('length: '))
#
#     if direction == 1:
#         print(symbol*length, end='')
#     else:
#         for i in range(length):
#             print(symbol)
#
# showing_direction_line(10,0,'^')



# Задание 4

z = 0

def simple_numbers(start: int, end: int):

    for i in range(start, end):
        global z
        z += 1
        if z % i == 0:
            print(i)

simple_numbers(1,10)

















