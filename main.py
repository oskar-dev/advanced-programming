# import data

from fastapi import FastAPI

from typing import List, Optional
from sqlalchemy import Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = "movies"

    movie_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    genres: Mapped[str] = mapped_column(String(255))

    def __init__(self, id: int, title: str, genres: list):
        self.movie_id = id
        self.title = title
        self.genres = "|".join(genres)

    def to_dict(self):
        return {
            "id": self.movie_id,
            "title": self.title,
            "genres": self.genres
        }

class Link(Base):
    __tablename__ = "links"

    link_id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.movie_id"))
    imdb_id: Mapped[Optional[int]] = mapped_column(Integer)
    tmdb_id: Mapped[Optional[int]] = mapped_column(Integer)

    def __init__(self, movie_id: int, imdb_id: int, tmdb_id: int):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

    def to_dict(self):
        return {
            "movie_id": self.movie_id,
            "imdb_id": self.imdb_id,
            "tmdb_id": self.tmdb_id
        }

class Rating(Base):
    __tablename__ = "ratings"

    rating_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.movie_id"))
    rating: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[int] = mapped_column(Integer)

    def __init__(self, user_id: int, movie_id: int, rating: float, timestamp: int):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "rating": self.rating,
            "timestamp": self.timestamp
        }

class Tag(Base):
    __tablename__ = "tags"

    tag_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.movie_id"))
    tag: Mapped[str] = mapped_column(String(255))
    timestamp: Mapped[int] = mapped_column(Integer)

    def __init__(self, user_id: int, movie_id: int, tag: str, timestamp: int):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "tag": self.tag,
            "timestamp": self.timestamp
        }

engine = create_engine("sqlite:///movies.db", echo=True)

Base.metadata.create_all(engine)

#  IMPORT DATA FROM CSV FILES INTO DATABASE
# with Session(engine) as session:

#     for movie in data.load_movies():
#         session.add(Movie(movie.movie_id, movie.title, movie.genres))

#     for link in data.load_links():
#         session.add(Link(link.movie_id, link.imdb_id, link.tmdb_id))

#     for rating in data.load_ratings():
#         session.add(Rating(rating.user_id, rating.movie_id, rating.rating, rating.timestamp))

#     for tag in data.load_tags():
#         session.add(Tag(tag.user_id, tag.movie_id, tag.tag, tag.timestamp))

#     session.commit()

app = FastAPI()

@app.get("/helloworld")
def get_hello_world():
    return {"Hello": "world"}

@app.get("/movies")
def get_movies():
    with Session(engine) as session:
        movies = session.query(Movie).all()
        return [movie.to_dict() for movie in movies]

@app.get("/links")
def get_links():
    with Session(engine) as session:
        links = session.query(Link).all()
        return [link.to_dict() for link in links]
    

@app.get("/ratings")
def get_ratings():
    with Session(engine) as session:
        ratings = session.query(Rating).all()
        return [rating.to_dict() for rating in ratings]
    

@app.get("/tags")
def get_tags():
    with Session(engine) as session:
        tags = session.query(Tag).all()
        return [tag.to_dict() for tag in tags]