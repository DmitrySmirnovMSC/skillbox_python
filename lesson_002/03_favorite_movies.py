#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код

len_movies = len(my_favorite_movies)
print(len_movies)

first_movie = my_favorite_movies[:10]
print(first_movie)

last_movie = my_favorite_movies[-15:]
print(last_movie)

second_movie = my_favorite_movies[12:25]
print(second_movie)

second_from_end_movie = my_favorite_movies[-22:-17]
print(second_from_end_movie)