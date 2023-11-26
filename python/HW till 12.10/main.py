# Задание 2

count_syms = 0
count_aa = 0
count_bb = 0
count_nums = 0
aa = ('аеёиоуыэюя')
bb = ('бвгджзйклмнпрстфчцчшщ')


with open('dano.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    for syms in text:
        if syms.isalpha():
            count_syms += 1

    file.seek(0)
    strings = len(file.readlines())

    for i_aa in text.lower():
        if i_aa in aa:
            count_aa += 1

    for i_bb in text.lower():
        if i_bb in bb:
            count_bb += 1

    for nums in text:
        if nums.isnumeric():
            count_nums += 1

with open('result.txt', 'w') as file_2:
    file_2.write(f'Количество символов: {count_syms}\n')
    file_2.write(f'Количество строк: {strings}\n')
    file_2.write(f'Гласные: {count_aa}\n')
    file_2.write(f'Согласные: {count_bb}\n')
    file_2.write(f'Количество цифр: {count_nums}\n')


print(f'Количество символов: {count_syms}')
print(f'Количество строк: {strings}')
print(f'Гласные: {count_aa}')
print(f'Согласные: {count_bb}')
print(f'Количество цифр: {count_nums}')






























