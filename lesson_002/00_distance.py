#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними

from pprint import pprint

moscow_x = sites['Moscow'][0]
moscow_y = sites['Moscow'][1]
london_x = sites['London'][0]
london_y = sites['London'][1]
paris_x = sites['Paris'][0]
paris_y = sites['Paris'][1]

moscow_to_london = ((moscow_x - london_x) ** 2 + (moscow_y - london_y) ** 2) ** 0.5
moscow_to_paris = ((moscow_x - paris_x) ** 2 + (moscow_y - paris_y) ** 2) ** 0.5
london_to_moscow = ((london_x - moscow_x) ** 2 + (london_y - moscow_y) ** 2) ** 0.5
london_to_paris = ((london_x - paris_x) ** 2 + (london_y - paris_y) ** 2) ** 0.5
paris_to_moscow = ((paris_x - london_x) ** 2 + (paris_y - london_y) ** 2) ** 0.5
paris_to_london = ((paris_x - moscow_x) ** 2 + (paris_y - moscow_y) ** 2) ** 0.5

# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

dist_from_moscow = {'to London': moscow_to_london, 'to Paris': moscow_to_paris,}
dist_from_london = {'to Moscow': london_to_moscow, 'to Paris': london_to_paris,}
dist_from_paris = {'to Moscow': paris_to_moscow, 'to London': paris_to_london,}

distances = {'from Moscow': dist_from_moscow, 'from London': dist_from_london, 'from Paris': dist_from_paris,}

# TODO здесь заполнение словаря

pprint(distances)
