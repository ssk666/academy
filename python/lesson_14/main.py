# Файлы

# file = open('filename.txt', 'r')  # просто прочитать файл

# file = open('filename.txt', 'w')  # записать файл (создать)

# file.write(f'Привет, я файл!\n')  # записать что-то в файл

# file = open('filename.txt', 'a')  # дозаписать 'a' - append

# file.write(f'Как ты? IIIMара???')


# file = open('filename.txt', 'r')  # чтобы прочитать что-то в файле, то нужно ставить флаг 'r'

# file = open('filename.txt', 'r+')  # открыть + записать

# file = open('filename.txt', 'w+')  # перезапись (удаление)


# for _ in range(5):
#     file.write('qq ^^\n')

# try:
#     text = file.readlines() # ищет по строкам (списковый формат)
#     raise ValueError
#     print(text)
# except ValueError:
#     file.close()
#     print('Поймали ошибку')
# finally:
#     print('Файл закрыт минуя все ошибки и закрывая наверняка')
#     file.close()

# file.close()  # закрытие файла


# filename_bin = open('file.bin', 'wb')  # write binary

# filename_bin.write('Мара - универсальный солдат'.encode())

# print(filename_bin.read().decode())

# filename_bin.close()


# контекстный менеджер, который самостоятельно закрывает выбранный файл
# with open('filename.txt', 'r') as file:
#     print(file.read())


# class CustomFile:
#     def __init__(self, file_name, mode):
#         self.file_name = file_name
#         self.mode = mode
#
#     def __enter__(self):
#         print('Сработал метод __enter__')
#         self.file = open(self.file_name, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Сработал метод exit')
#         self.file.close()
#
# with CustomFile('filename.txt', 'r') as file:
#     pass
#


# Задание 1
# import random
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
#
# def caesar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33]
#                        if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
#
#
# with open('text.txt', 'w', encoding='utf-8') as file_1:
#     for _ in range(5):
#         file_1.write('Привет\n')
#
#
# with open('cipher_text.txt', 'a', encoding='utf-8') as file_2:
#     with open('text.txt', 'r', encoding='utf-8') as file_1:
#         lines = file_1.readlines()
#         shift = random.randint(1, 10)
#         for i_line in lines:
#             ciphered = caesar_code(i_line.strip(), shift)
#             # file_2.write(ciphered + '\n')
#             # shift += 1
#             file_2.write(ciphered[:len(ciphered) // 2] + f'({shift})' + ciphered[len(ciphered) // 2:] + '\n')



# Задание 2

# freq = {}
#
# with open('zen.txt', 'r') as file:
#     text = file.read().lower()
#     # print(freq)
#
# # 2 вариант через генератор
#     freq = {sym: text.count(sym) for sym in text if sym.isalpha()}
# # print(freq)
#
#     alpha_num = len(freq.keys())
#     total_num = sum(freq.values())
#     min_alpha = min(freq.values())
#     file.seek(0) # отправить курсор в начало документа (0) - это позиция
#     lines_num = len(file.readlines())
#     words_num = len(text.split(' '))
#     print(alpha_num, total_num, min_alpha, lines_num, words_num)




# Задание 3


# with open("zen.txt", "w+") as file:
#     rev_zen = file.readlines()[::-1]
#     for i in rev_zen:
#         print(i.strip())
#         file.write(i.strip())
# file = open('filename.txt', 'w+')  # перезапись



# Задание 4

with open('bad_words.txt', 'r') as file_1:
    with open('text.txt', 'r') as file_2:
        text = file_2.read()
        for bad in file_1.readlines():
            if bad.strip() in text:
               text = text.replace(bad, '')
    with open('text.txt', 'w') as file_2:
        file_2.write(text)
































