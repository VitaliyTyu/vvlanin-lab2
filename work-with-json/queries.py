import json

# Загрузка JSON
with open("movies.json", "r") as file:
    data = json.load(file)


# 1. Получить все фильмы указанного жанра (например, Drama):
genre = "Drama"
movies_with_genre = [movie for movie in data["movies"] if genre in movie["genres"]]

print(f"\nФильмы жанра {genre}:")
for movie in movies_with_genre:
    print(movie["title"])


# Получить все фильмы с актёрским составом более пяти человек:
movies_with_large_cast = [movie for movie in data["movies"] if len(movie["cast"]) > 5]

print("\nФильмы с актёрским составом более 5 человек:")
for movie in movies_with_large_cast:
    print(movie["title"])


# 3. Получить все фильмы, где человек является режиссёром и актёром одновременно (например, Quentin Tarantino):

person = "Quentin Tarantino"
movies_with_actor_director = [
    movie for movie in data["movies"]
    if person in movie["directors"] and person in movie["cast"]
]

print(f"\nФильмы, где {person} является режиссёром и актёром одновременно:")
for movie in movies_with_actor_director:
    print(movie["title"])
    
    

# 4. Сформировать случайный список просмотра из заданного количества фильмов указанного жанра (например, 3 фильма жанра Drama):

import random

count = 3
random_movies = random.sample(movies_with_genre, min(count, len(movies_with_genre)))

print(f"\nСлучайные {count} фильма жанра {genre}:")
for movie in random_movies:
    print(movie["title"])


# 5. Pапрос с использованием функций:
# Пример: посчитать общее число зрителей всех фильмов в жанре "Drama".

total_viewers = sum(movie["viewers"] for movie in movies_with_genre)

print(f"\nОбщее число зрителей для фильмов жанра {genre}: {total_viewers}")


print()

# Доп. Функции для универсальных запросов в JSON:
def filter_by_genre(data, genre):
    return [movie for movie in data["movies"] if genre in movie["genres"]]

def filter_by_cast_size(data, size):
    return [movie for movie in data["movies"] if len(movie["cast"]) > size]

def filter_by_director_and_actor(data, person):
    return [
        movie for movie in data["movies"]
        if person in movie["directors"] and person in movie["cast"]
    ]

# Пример использования:
print(filter_by_genre(data, "Thriller"))
