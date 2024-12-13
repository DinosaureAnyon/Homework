x = float(input('Введите делимое\n'))
y = float(input('Введите делитель\n'))
if y == 0:
    print('Деление на 0 не возможно')
else:
    print(f'Частное {x/y}')



a = float(input('Введите сумму покупок\n'))
if a < 20:
    print('А вот нет скидки')
else:
    print(f'Скидка: -35% {round(a / 100 * 35)} у.е. \nИтог: {round(a - a / 100 * 35)}')



import calendar
j = int(input('Введите номер месяца\n'))
if j not in range(1, 13):
    print('Нет такого месяца')
else:
    print(calendar.month_name[j])
