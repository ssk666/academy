# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6 , 7, 8]

# print(list_1 + list_2) # объединение список - 123455678
# print(list_1 * 2)

# list_1.extend(list_2) # то же самое как сложение, только расширение списка
# print(list_1)

# list_3 = ['1', '2', '3', '4']
# string = ',' # каким символом перечислять
# new_string = string.join(list_3) # присоединили к пустой строке список
# # второй вариант через for
# for i in list_3:
#     string += f' {i}'
# print(new_string)



# list_1 = [i for i in range(1, 10)]  # 1-я i - это переменная, потом чем будет наполнять - это for
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list_1)

# list_1 = [i for i in range(1, 10) if i % 2 == 0] #УМЕСТИТЬ В ОДНУ СТРОКУ ЧИСЛА КРАТНЫЕ 2

# list_1 = [i ** 2 for i in range(1, 10)] #квадраты чисел из диапазона

# list_2 = [i for i in range(1, 5) for _ in range (5)] #дубликаты числел, то есть каждое число по сколько-то раз вывести
# list_2 = [[i for i in range(1, 5)] for _ in range (5)] #поместили список в список
# list_3 = [i * j for i in range(1, 5) for j in range(1, 5)] # ответ - [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16]
# print(list_3)

# list_4 = [35, 7, 4, 87, 65]
# list_5 = [num for num in list_4 if num % 7 == 0] # проверили каждое число из списка, которое кратно 7

# import string
# letters = string.ascii_letters
#
# input_text = 'he1ll1o m$a N81*ame is M@arA@'
# letters_list = [letter for letter in input_text if (letter in letters or letter == ' ')]
# # переменная + что сделать + если наш символ есть в разрешенных или этот символ является пробелом
# print(''.join(letters_list)) # '' - это пустая строка, к которой мы просто приписываем объекты



# import string
#
# digits = string.digits
#
# input_text = 'fdsfnjf 3k4j kf 34 f34k fk2 34kj 24f jkrbjksfskefsj228 s999ss s666s'
# digits_list = [nums for nums in input_text if (nums in digits)]
# print(''.join(digits_list), len(digits_list))



# students = [
#     ['Габитов', 7.7],
#     ['Падурин', 9.9],
#     ['Николаев', 6.6],
#     ['Маркелов', 2.2],
#     ['Саитов', 3.3],
# ]
#
# avg_list = [avg for avg in students if avg[1] >= 4.5]
# # 2 элемента в списке, фамилия + оценка, то есть фамилия[0], а оценка[1]
# print(avg_list)



















