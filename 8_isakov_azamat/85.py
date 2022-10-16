# Вычисляем длину гипотенузы. Напишите функцию, принимающую на вход длины двух катетов прямоугольного треугольника и возвращающую длину гипотенузы, рассчитанную по теореме Пифагора.
from math import sqrt


def find_hypot(a, b):
    c = sqrt(a ** 2 + b ** 2)
    print(f'The hypotenuse of the legs is three {c}')


a = float(input('Enter first leg: '))
b = float(input('Enter second leg: '))
find_hypot(a, b)
