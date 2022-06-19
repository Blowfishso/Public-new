tikets = int(input('Введите количество билетов: '))
count = 0
age = [int(input('Введите возраст: ')) for i in range(tikets)]
for i in range(tikets):
    if age[i] < 18:
        count += 0
    elif 18 <= age[i] < 25:
        count += 900
    elif age[i] >= 25:
        count += 1390
if tikets > 3:
    print(f'Сумма к оплате {count * 0.9} руб.')
else:
    print(f'Cумма к оплате {count} руб.')