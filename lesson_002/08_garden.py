#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
print(garden_set)
meadow_set = set(meadow)
print(meadow_set)

# выведите на консоль все виды цветов
# TODO здесь ваш код
merge_garden_meadow = garden_set | meadow_set
print(merge_garden_meadow)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
intersection_garden_meadow = garden_set & meadow_set
print(intersection_garden_meadow)

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
subtraction_garden_meadow = garden_set - meadow_set
print(subtraction_garden_meadow)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
subtraction_meadow_garden = meadow_set - garden_set
print(subtraction_meadow_garden)