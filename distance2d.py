"""Напишите программу, которая принимает на вход координаты двух точек и находит
 расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21"""

from math import sqrt


def InDate():
    xyz = ["A X", "A Y", "B X", "B Y"]
    numb = []
    for i in xyz:
        numb.append(int(input(f"Введите {i} :")))
    return numb


def Distance(numb):
    a = [numb[0], numb[1]]
    b = [numb[2], numb[3]]
    x = b[0]-a[0]
    y = b[1]-a[1]
    ab = sqrt((x**2)+(y**2))
    return ab


print(round(Distance(InDate()), 2))
