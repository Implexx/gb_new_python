"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""

x_coord = int(input('Введите числовое значение координаты X = '))
y_coord = int(input('Введите числовое значение координаты Y = '))

if x_coord or y_coord != 0:
    if x_coord == 0:
        print(f'Точка ({x_coord}:{y_coord}) находится на оси Y')
    elif y_coord == 0:
        print(f'Точка ({x_coord}:{y_coord}) находится на оси Х')
    elif x_coord > 0 and y_coord > 0:
        print(f'Точка ({x_coord}:{y_coord}) находится на 1 четверти')
    elif x_coord < 0 and y_coord > 0:
        print(f'Точка ({x_coord}:{y_coord}) находится на 2 четверти')
    elif x_coord < 0 and y_coord < 0:
        print(f'Точка ({x_coord}:{y_coord}) находится на 3 четверти')
    elif x_coord > 0 and y_coord < 0:
        print(f'Точка ({x_coord}:{y_coord}) находится на 4 четверти')
else:
    print('Введенные координаты равны нулю')