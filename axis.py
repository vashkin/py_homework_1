# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка(или на какой оси она находится).
# Пример:
# - x = 34; y = -30 -> 4
# - x = 2; y = 4 -> 1
# - x = -34; y = -30 -> 3


def received_data():
    xyz = ["X", "Y"]
    received_number = []

    for i in xyz:
        received_number.append(int(input(f"Введите {i} :")))
    return received_number


def axis_coordinate(received_number):

    if received_number[0] < 0 and received_number[1] > 0:
        axis = 2
    elif received_number[0] > 0 and received_number[1] > 0:
        axis = 1
    elif received_number[0] < 0 and received_number[1] < 0:
        axis = 3
    elif received_number[0] > 0 and received_number[1] < 0:
        axis = 4
    else:
        print("!!!координата не может быть '0' !!!")
        axis = axis_coordinate(received_data())
    return axis


print(axis_coordinate(received_data()))
