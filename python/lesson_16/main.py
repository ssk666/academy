# a = set()  # создать множество
# a.add('apple')  # добавить что-то в множество
# a.add('apple')  # одно и то же не добавит, тк это уже есть
# print(a)

# print(a[0])  # по индексам нельзя обращаться + считать элементы

# print('banana' in a)  # проверка на вхождение

# a.remove('apple')  # удалить что-то из множества
# a.discard('apple')  # тоже удаляет, но если нет такого элемента, то ошибку не выкинет
# a.pop() # удаляет любой элемент (рандом)


# b = {'orange', 'watermelon', 'grape', 'lemon'}  # так тоже можно создавать множества

# print(a.intersection(b))  # получим пустое значение, тк нет пересечений
# b = {'orange', 'apple'}
# print(a.intersection(b)) # ответ - apple

# print(a.difference(b))  # ответ apple - тк в множестве b нет элемента apple
# print(b.difference(a))  # ответ orange, water,elon - тк в множестве a нет этих элементов

# c = a.union(b)  # объединение множеств (создает новое множество)
# print(a.union(b))  # объединение множеств

# a.clear()  # очистить множество
# print(a)

# a.update(b)  # обновляет множество другим множеством (изменяет текущее множество)
# print(a)

# for item in a:  # можно проходиться по множествам
#     print(item)
#
# print(*a)  # распаковка множества как со списками тоже работает

# print('-'.join(b))  # добавлять тоже можно

# set_1 = {['Name'], 18, {'key': 'value'}}  # будет ошибка, тк во множествах могут храниться только простые типы данных
# print(set_1)



# list_1 = ['apple', 'orange']  # 72 бита памяти
# set_1 = {'apple', 'orange'}  # 216 бита памяти

# print(set_1.update(list_1))  # множество нельзя обновить списком



# with open ('lorem.txt', 'r') as file:
#     text = file.read()
#     set_text = set(text)
#     print(len(set_text))



# data = {}
#
# with open('voyna-i-mir.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     symbols = set(text)
#     file.seek(0)
#     for sym in symbols:
#         if sym.isalpha():
#             data[sym] = text.count(sym)
#     sorted_dict = sorted(data, key=lambda x: data[x], reverse=True)
#     print(data['о'])
# print(sorted_dict)



# string = 'acccccdad'
#
#
# def check(string):
#     data = {}
#     for i in string:
#         data.setdefault(i, 0)
#         data[i] += 1
#
#     count = 0
#     for j in data.values():
#         if j % 2 != 0:
#             count += 1
#
#     if count <= 1:
#         print('Может')
#     else:
#         print('Не может')
#
# check(string)



 # Генераторы

# list_1 = [i for i in range(100)]  # 920 бит
# print(list_1)

# generation = (i for i in range(100))  # генераторное выражение; 104 бита
# for i in generation:
#     print(i)


# def custom_range(start, end):
#     for i in range(start, end):
#         yield i  # генератор
#
#
# for i in custom_range(10, 20):
#     print(i)


# class Generator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.cur = start
#
#     def __iter__(self):
#         print('__iter__')
#         return self
#
#     def __next__(self):
#         print('__next__')
#         if self.cur == self.end:
#             raise StopIteration
#         self.cur += 1
#         return self.cur
#
#
# for i in Generator(10, 20):
#     print(i)



# with open('haha.txt', 'r') as file:
#      words = list(i_word for i_word in file.readlines())  # генератор можно преобразовать в ту структуру данных, в которую нужно
    # words = set(i_word for i_word in file.readlines())

# for i in words:
#     print(i.strip())




# def words():
#     with open('haha.txt', 'r') as file:
#         for i in file.readlines():
#             yield i
#
# for i in words():
#     print(i.strip())




# Бесконечный генератор

# def infinity():
#     while True:
#         yield 1
#
#
# for i in infinity():
#     print(i)




# Список имен, в котором есть буква "А"

list = ['Марат', 'Степан', 'Артем', 'Анатолий', 'Дэн']

gen = (i for i in list if 'а' in i.lower())

print(*gen)











































