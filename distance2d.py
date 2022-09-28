"""Напишите программу, которая принимает на вход координаты двух точек и находит
 расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21"""

from math import sqrt


def received_data():
    xyz = ["A X", "A Y", "B X", "B Y"]
    received_number = []
    for i in xyz:
        received_number.append(int(input(f"Введите {i} :")))
    return received_number


def Distance(received_number):
    a = [received_number[0], received_number[1]]
    b = [received_number[2], received_number[3]]
    x = b[0]-a[0]
    y = b[1]-a[1]
    ab = sqrt((x**2)+(y**2))
    return ab


print(round(Distance(received_data()), 2))
