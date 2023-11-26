# Задача 9
# time = int(input('Введи число в часах:'))
# if 7 <= time <= 10:
#     print('Wake up!')
# elif time < 0 or time > 23:
#     print('Error')
# else:
#     print('U wasted')
#
# Задача 8
# first = int(input('Enter the first score: '))
# second = int(input('Enter the second score: '))
# third = int(input('Enter the third score: '))
# allin = first + second + third
# if allin >= 250:
#     print('Success')
# else:
#     print('U r stupido')

# Задача 7
# mins = int(input('Enter the mins: '))
# hours = mins // 60
# minutes_yet = mins % 60
# print(f'{hours} часов, {minutes_yet} минут')

# ЦИКЛЫ
# for i in range(10):
#     print(i)
# i - это просто переменная

# for _ in range(10):
    # print('Hello') - если не используем снизу, то ставить прочерк

# for i in 'python':
    # print(i + '*', end="") end='' - отмена переноса строки; i + '' - это добавить что-то

# for i in range (0, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print('ok')

# start = int(input('Enter the start: '))
# end = int(input('Enter the end: '))
#
# for i in range(start, end + 1): -- +1 это потому что в конце меньше на 1, тк счет начинается с 0
#     if i % 2 == 0:
#         print(f'{i} is even')
#
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         print(f'{i} is odd')

# start = int(input('Enter the start: '))
# end = int(input('Enter the end: '))
# for i in range(end, start - 1, -2):
#     print(i)

# summa = 0
# for i in range (1, 100):
#     summa += i -- (число прибавляется и приравнивается, summa = summa + i)
# print(f'Summa ryada = {summa}')

# first = int(input('Enter the first num: '))
# second = int(input('Enter the second num: '))
#
# summa = 0
# count = 0
# for i in range(first, second + 1):
#     summa += i
#     count += 1
#
# print(f'Сумма ряда {summa}')
# print(f'СРЗНАЧ = {summa / count}')


# Факториал
# 3! = 1*2*3 = 6
# 4! = 1*2*3*4 = 24

# num4ik = int(input('Enter a num: '))
# fucktorial = 1
# for i in range(2, num4ik + 1):
#     fucktorial *= i
# print(f'FaCTORIAL OF THE NUM {num4ik} = {fucktorial}')


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end='\t')
#     print() - переход на новую строку


# correct_pin = 1547
#
# for i in range(3):
#     pin = int(input('Enter the PIN: '))
#     if pin == correct_pin:
#         print('Success!')
#         break
#     else:
#         print('Try again...')
# else:
#     print('You tried 3 times with no success, your card is blocked')


# length = int(input('Enter the length of the line: '))
# for i in range(length):
#     print('*', end='')


# length = int(input('Enter the length of the line: '))
# sym = input('Put the symbol: ')
# for i in range(length):
#     print(sym, end='')


start = int(input('start from: '))
end = int(input('end to: '))
number = int(input('put the num: '))

for i in range(start, end + 1):
    if i == number:
        print(f'!{i}!', end='')
        continue
    print(i, end=' ')




















































































