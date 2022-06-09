money = float(input('Введите сумму вклада: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

b1 = per_cent.get('ТКБ')
Bank1 = round(b1 / 100 * money)
b2 = per_cent.get('СКБ')
Bank2 = round(b2 / 100 * money)
b3 = per_cent.get('ВТБ')
Bank3 = round(b3 / 100 * money)
b4 = per_cent.get('СБЕР')
Bank4 = round(b4 / 100 * money)

deposit = [Bank1, Bank2, Bank3, Bank4]
max_percent = max(deposit)
print(deposit)
print('Максимальная сумма, которую вы можете заработать -', max_percent)
