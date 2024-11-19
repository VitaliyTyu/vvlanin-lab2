from lxml import etree
import random

# Загрузка XML
xml_file = "movies.xml"
tree = etree.parse(xml_file)
root = tree.getroot()

# XPath-запросы
def get_movies_by_genre(tree, genre):
    """Получить все фильмы указанного жанра."""
    xpath_query = f"//movie[genres/genre[text()='{genre}']]"
    return tree.xpath(xpath_query)

def get_movies_with_large_cast(tree, min_cast_size):
    """Получить фильмы с актёрским составом больше указанного размера."""
    xpath_query = f"//movie[count(cast/person) > {min_cast_size}]"
    return tree.xpath(xpath_query)

def get_movies_with_actor_director(tree, person):
    """Получить фильмы, где человек является режиссёром и актёром."""
    xpath_query = f"//movie[directors/director[text()='{person}'] and cast/person[text()='{person}']]"
    return tree.xpath(xpath_query)

def random_watchlist(tree, genre, count):
    """Сформировать случайный список фильмов указанного жанра."""
    movies = get_movies_by_genre(tree, genre)
    return random.sample(movies, min(count, len(movies)))

def count_total_actors(tree):
    """Посчитать общее количество актёров во всех фильмах."""
    xpath_query = "count(//movie/cast/person)"
    return int(tree.xpath(xpath_query))

# Примеры использования
if __name__ == "__main__":
    # 1. Фильмы жанра "Drama"
    genre = "Drama"
    movies = get_movies_by_genre(tree, genre)
    print(f"Фильмы жанра {genre}:")
    for movie in movies:
        print(movie.find("title").text)

    # 2. Фильмы с актёрским составом больше 5 человек
    large_cast_movies = get_movies_with_large_cast(tree, 5)
    print("\nФильмы с актёрским составом больше 5 человек:")
    for movie in large_cast_movies:
        print(movie.find("title").text)

    # 3. Фильмы, где Quentin Tarantino режиссёр и актёр
    person = "Quentin Tarantino"
    actor_director_movies = get_movies_with_actor_director(tree, person)
    print(f"\nФильмы, где {person} режиссёр и актёр:")
    for movie in actor_director_movies:
        print(movie.find("title").text)

    # 4. Случайный список просмотра из 2 фильмов жанра "Drama"
    watchlist = random_watchlist(tree, genre, 2)
    print("\nСлучайный список просмотра (жанр Drama):")
    for movie in watchlist:
        print(movie.find("title").text)

    # 5. Общее количество актёров во всех фильмах
    total_actors = count_total_actors(tree)
    print(f"\nОбщее количество актёров во всех фильмах: {total_actors}")
