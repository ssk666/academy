# Задание 1

# violator_songs = {
# 'World in My Eyes': 4.86,
# 'Sweetest Perfection': 4.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.9,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.20,
# 'Policy of Truth': 4.76,
# 'Blue Dress': 4.29,
# 'Clean': 5.83
# }
#
# ask = int(input('Сколько выбрать песен: '))
# summ = 0
# for i in range(ask):
#     song = input('Название {} песни: '.format(i + 1))
#     if violator_songs.get(song):
#         summ += violator_songs.get(song)
#     else:
#         print('Данная песня отсутствует')
# print(f'Общее время {summ} минут')


# Задание 2

# data = {
# "address": "0x544444444444",
# "ETH": {
# "balance": 444,
# "totalIn": 444,
# "totalOut": 4
# },
# "count_txs": 2,
# "tokens": [
# {
# "fst_token_info": {
# "address": "0x44444",
# "name": "fdf",
# "decimals": 0,
# "symbol": "dsfdsf",
# "total_supply": "3228562189",
# "owner": "0x44444",
# "last_updated": 1519022607901,
# "issuances_count": 0,
# "holders_count": 137528,
# "price": False
# },
# "balance": 5000,
# "totalIn": 0,
# "total_out": 0
# },
# {
# "sec_token_info": {
# "address": "0x44444",
# "name": "ggg",
# "decimals": "2",
# "symbol": "fff",
# "total_supply": "250000000000",
# "owner": "0x44444",
# "last_updated": 1520452201,
# "issuances_count": 0,
# "holders_count": 20707,
# "price": False
# },
# "balance": 500,
# "totalIn": 0,
# "total_out": 0
# }
# ]
# }
#
#
# print(data.items())
#
# data['total_diff'] = 100
# data['tokens'][0]['fst_token_info']['name'] = 'doge'
# data['ETH']['total_out'] = data['tokens'][0].pop('total_out')
# data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
#
# print(data.items())
