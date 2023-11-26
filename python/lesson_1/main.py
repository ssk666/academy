# print("Hello world!")

# sep всегда указывается в кавычках
# \n - перенос на новую строчку
# \t - табуляция
# print("Hello", "Mara", "!", sep="\t")

# print('Hello Python!', end=' ')
# print('Hello Ruby!')
# print('Hello Java!')

# number_1 = 50
# number_2 = 75

# print ()

# name = input('Enter your name: ')
# age= int(input('Enter your age: '))
# print('Hello, ' + name + '!' + ' Tebe already ' + str(age) + ' old...') - очень не Гибко
# print('Hello, {val_1} ! Tebe already {val_2} old...'.format(val_1=name, val_2=age)) - старый метод, но может встретиться
# print('Hello, {0} ! Tebe already {1} old...'.format(name, age)) - тоже старый
# print(f'Hello, {name}! Tebe already {age} old...') - THE NEWEST

# nomer = input('Введите число: ')

# Задача 1
# number = int(input('Введите трехзначное число: '))
# first_num = number // 100
# print(print(first_num))
#
# second_num = number // 10 % 10
# print(second_num)
#
# third_num = number % 10
# print(third_num)
# # Преобразовали в format
# print(f'{first_num}\n{second_num}\n{third_num}\n{first_num+second_num+third_num}')

# import time
# print (time.time() // 3600 // 24 // 365)


# Задача 3
# number_1 = (input('Введи первое число: '))
# number_2 = (input('Введи второе число: '))
# print (number_1 + number_2)

# Задача 4
# temp_cel = float(input('Введи температуру по цельсию: '))
# print ((temp * 1.8) + 32)

# Задача от Некита
# sam = int(input('Введи четырехзначное число: '))
# sam_1 = sam // 1000
# print(sam_1)
# sam_2 = sam // 100 % 10
# print(sam_2)
# sam_3 = sam // 10 % 10
# print(sam_3)
# sam_4 = sam % 10
# print(sam_4)
# num = sam_1*sam_2*sam_3*sam_4
# print (num)


# Задача на проходку в Ebay
num = int(input('Введи число от 1 до 100: '))
if num < 1 or num > 100:
    print('ERROR')
if((num % 3 == 0):
    print ('Fizz')

# leetcode.com
# Сам себе программист Кори Альтхоф
# Операционные системы 4 издание Танненбаум 1000стр
# Программист-прагматик














