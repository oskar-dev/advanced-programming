from fastapi import FastAPI

import db

app = FastAPI()

moveies = db.load_movies();

@app.get("/helloworld")
def get_hello_world():
    return {"Hello": "world"}

@app.get("/movies")
def get_movies():
    return [movie.__dict__() for movie in moveies]

@app.get("/links")
def get_links():
    return [link.__dict__() for link in db.load_links()]

@app.get("/ratings")
def get_ratings():
    return [rating.__dict__() for rating in db.load_ratings()]

@app.get("/tags")
def get_tags():
    return [tag.__dict__() for tag in db.load_tags()]