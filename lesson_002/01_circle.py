#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код

radius = 42
number_pi = 3.1415926
area_of_circle = number_pi * (radius ** 2)
area_of_circle_round = round(area_of_circle, 4)
print(area_of_circle_round)

# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
# TODO здесь ваш код

x_point = point[0]
y_point = point[1]
x_circle_center = int(input('Введите значение x: '))
y_circle_center = int(input('Введите значение y: '))

equation = (x_point - x_circle_center)**2 + (y_point - y_circle_center)**2 <= radius**2
print(equation)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код

x_point_2 = point_2[0]
y_point_2 = point_2[1]

equation_2 = (x_point_2 - x_circle_center)**2 + (y_point_2 - y_circle_center)**2 <= radius**2
print(equation_2)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False
