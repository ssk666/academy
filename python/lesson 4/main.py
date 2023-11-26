# count = 0
#
# while count <=5:
#     count += 1
#     print(count)
#
#
# count = 0
#
# while True: - бесконечный цикл, затем прерываем его брейком
#     count += 1
#     print(count)
#     if count == 5:
#         break

# number = int(input('Enter the number: '))
# factorial = 1
#
# while number >= 1:
#     factorial *= number
#     number -= 1
#
# print(factorial)

# summa = 0
# while True:
#     number = float(input('Enter the number or 0 to end a cycle: '))
#     if number == 0:
#         print(summa)
#         break
#     summa += number



# debt = 1000
# attempts = 3
# while debt > 0:
#     money = int(input(f'Your debt is {round(debt,2)}, how much you can dep?: '))
#
#     if money <= 0:
#         print('Summ cannot be less or equal to 0')
#         continue
#     if attempts > 0:
#         debt -= money
#     else:
#         print('Be ready for %%% :D')
#         debt *= 1.1
#         debt -= money
#     attempts -= 1
# print('You close a debt')



# import random
# pick = int(input('What the level do you want? 1/2:'))
#
# flag = True
#
# print('Check ur knowledge!')
# while flag:
#     if pick == 1:
#         number_1 = random.randint(1, 10)
#         number_2 = random.randint(1, 10)
#
#     else:
#         number_1 = random.randint(10, 20)
#         number_2 = random.randint(10, 10)
#
#     result = number_1 * number_2
#     answer = int(input(f'{number_1} * {number_2} = '))
#     while answer != result:
#         print('False! Try again...')
#         answer = int(input(f'{number_1} * {number_2} = '))
#     else:
#         print('Nice!')
#
#
#     choice = input('Continue? Y/N: ')
#     if choice == 'n':
#         print('Bye-bye')
#         flag = False

# import random
#
# attempts = 2
# guess = random.randint(1, 100)
# guessed = False
#
# while not guessed:
#
#     if attempts == 0:
#         break
#     number = int(input('Guess the num from 1 to 100: '))
#
#
#
#     if number == guess:
#         print('You guessed')
#         guessed = True
#     elif number > guess:
#         print('less')
#     elif number < guess:
#         print('more')
#     elif attempts == 0:
#         print('end')
#
#     attempts -= 1


# Задание 1:
#
# x = int(input('Введи число x: '))
# y = int(input('Введи число y^: '))
# result = 1
#
# while y > 0:
#     result *= x
#     y -= 1
# print (result)
#
# Задание 2:

count = 0
for i in range (100, 1000)




































