import csv

class Movie():
    def __init__(self, id: int, title: str, genres: list):
        self.movie_id = id
        self.title = title
        self.genres = genres

    def __dict__(self):
        return {
            "id": self.movie_id,
            "title": self.title,
            "genres": "|".join(self.genres)
        }

class Link():
    def __init__(self, movie_id: int, imdb_id: str, tmdb_id: str):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

    def __dict__(self):
        return {
            "movie_id": self.movie_id,
            "imdb_id": self.imdb_id,
            "tmdb_id": self.tmdb_id
        }

class Rating():
    def __init__(self, user_id: int, movie_id: int, rating: float, timestamp: int):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

    def __dict__(self):
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "rating": self.rating,
            "timestamp": self.timestamp
        }

class Tag():
    def __init__(self, user_id: int, movie_id: int, tag: str, timestamp: int):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

    def __dict__(self):
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "tag": self.tag,
            "timestamp": self.timestamp
        }

def load_movies() -> list:
    movies = []
    with open("data/movies.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            id = int(row[0])
            title = row[1]
            genres = row[2].split("|")
            
            movies.append(Movie(id, title, genres))
    return movies

def load_links() -> list:
    links = []
    with open("data/links.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            movie_id = int(row[0])
            imdb_id = row[1]
            tmdb_id = row[2]

            links.append(Link(movie_id, imdb_id, tmdb_id))
    return links

def load_ratings() -> list:
    ratings = []
    with open("data/ratings.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            user_id = int(row[0])
            movie_id = int(row[1])
            rating = float(row[2])
            timestamp = int(row[3])

            ratings.append(Rating(user_id, movie_id, rating, timestamp))
    return ratings

def load_tags() -> list:
    tags = []
    with open("data/tags.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            user_id = int(row[0])
            movie_id = int(row[1])
            tag = row[2]
            timestamp = int(row[3])

            tags.append(Tag(user_id, movie_id, tag, timestamp))
    return tags