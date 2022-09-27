"""Напишите программу, которая принимает на вход координаты точки (X и Y),
 причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
  эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4 -> 1
- x=-34; y=-30 -> 3"""


def InDat():
    xyz = ["X", "Y"]
    numb = []

    for i in xyz:
        numb.append(int(input(f"Введите {i} :")))
    return numb


def AxisC(numb):

    if numb[0] < 0 and numb[1] > 0:
        axis = 2
    elif numb[0] > 0 and numb[1] > 0:
        axis = 1
    elif numb[0] < 0 and numb[1] < 0:
        axis = 3
    elif numb[0] > 0 and numb[1] < 0:
        axis = 4
    else:
        print("!!!координата не может быть '0' !!!")
        axis = axisC(inDat())
    return axis


print(AxisC(InDat()))
