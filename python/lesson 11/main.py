# Словари

# dictionary = {'name': 'Marat', 'age': 21}
#
# name = dictionary.get('name') # вызов по ключу
# dictionary['age'] = 33 # изменения значения по ключу
# dictionary['surname'] = 'Gab'  # добавление ключа + значения
# dictionary.pop('age') # удалили ключ вместе со значением

# print(dictionary.keys()) # какие ключи есть в словаре
# print(dictionary.values()) # какие значения есть в словаре
# print(dictionary.items()) # какие есть ключи, значения (все вместе)

# dictionary_2 = {'name': 'Stepa', 'age': 27}
# dictionary.update(dictionary_2) #обновили данные в списке (прибавляет значения)
# dictionary.setdefault('address', '') # выставляет значение по умолчанию (если ключа изначально нет)
# print(dictionary)



# dictionary = {}
# def set_country(country):
#     dictionary.setdefault(country, [])
#     print('Страна добавлена')
#
# def set_city():
#     key = input('Страна: ')
#     country = dictionary.get(key)
#     city_name = input('Введите название города: ')
#     if country or country == []:
#         for i_city in country:
#             if city_name in i_city.keys():
#                 print('Такой город уже есть!')
#                 return
#         population = int(input('Введите населения города: '))
#         time_zone = input('Введите часовой пояс: ')
#         new_city = {city_name: {'population': population, 'time_zone': time_zone}}
#         dictionary[key].append(new_city)
#         print('Город добавлен')
#     else:
#         print('Такой страны - нет')
#
# def get_city_info():
#     country = input('Страна: ')
#     get_country = dictionary.get(country)
#     if get_country:
#         city = input('Введите название города: ')
#         for i_city in get_country:
#             if city in i_city.keys():
#                 city_info = i_city[city]
#                 print(f'Население города: {city_info.get("population")}\n'
#                       f'Часовой пояс: {city_info.get("time_zone")}')
#                 return
#     else:
#         print('Такого города - нет')
#
#
# def main():
#     while True:
#         choice = input('Add country - 1: \n'
#                        'Add city - 2 : \n'
#                        'Get info of city - 3: \n'
#                        'Enter: ')
#         if choice == '1':
#             country = input('Введи название страны: ')
#             set_country(country)
#
#         elif choice == '2':
#             set_city()
#         elif choice == '3':
#             get_city_info()
#
# main()



# text = input('Введите текст: ')
# freq_dict = {}
# for i_sym in text:
#     if not i_sym.isspace():
#         freq_dict.setdefault(i_sym, 0)
#         freq_dict[i_sym] += 1
# print(freq_dict)
# #каждая буква с каждой новой строчки
# for key, value in freq_dict.items():
#     print(f'{key}: {value}')



# без setdefault
# text = input('Введите текст: ')
# freq_dict = {}
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         if i_symbol in freq_dict.keys():
#             freq_dict[i_symbol] += 1
#         else: freq_dict[i_symbol] = 1
#
# for key, value in freq_dict.items():
#     print(f'{key}: {value}')


# text = input('Введите текст: ')
# freq_dict = {}
# count = 0
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         count = text.count(i_symbol)
#         freq_dict.setdefault(count, [])
#         if i_symbol not in freq_dict[count]:
#             freq_dict[count].append(i_symbol)
# for key, value in freq_dict.items():
#     print(f'{key}: {value}')


# пригодится для дз
dict_1 = {
    'key': {
        'key_2': {
            'key_3': 125,
            'key_4': {
                'key_5': 'hello'
            }
        }
    }
}

print(dict_1['key']['key_2']['key_3'])

































