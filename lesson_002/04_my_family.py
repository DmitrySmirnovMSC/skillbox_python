#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Наталья', 'Роман', 'Игорь', 'Степа']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Наталья', 165],
    ['Роман', 172],
    ['Игорь', 176]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

height_Igor = str(my_family_height[2][1])
print("Рост Игоря - " + height_Igor + " см")

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

sum_heights_my_family = str(my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1])
print("Общий рост моей семьи - " + sum_heights_my_family + " см")