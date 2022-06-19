tickets = int(input('Enter the number of tickets: '))
count = 0
age = [int(input('Age of visitor: ')) for i in range(tickets)]
for i in range(tickets):
    if age[i] < 18:
        count += 0
    elif 18 <= age[i] < 25:
        count += 900
    elif age[i] >= 25:
        count += 1390
if tickets > 3:
    print(f'Total sum - {count * 0.9} RUB')
else:
    print(f'Total sum - {count} RUB')
