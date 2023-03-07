# === Database interaction file ===
import sqlite3

CREATE_MOVIES_TABLE = "CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, rating INTEGER);"

INSERT_MOVIE = "INSERT INTO movies (title, year, director, rating) VALUES (?, ?, ?, ?);"

GET_ALL_MOVIES = "SELECT * FROM movies;"
GET_TOP_MOVIES = "SELECT * FROM movies ORDER BY rating DESC;"
GET_MOVIES_BY_TITLE = "SELECT * FROM movies WHERE title = ?;"
GET_BEST_MOVIE_OF_DIRECTOR = """
SELECT * FROM movies
WHERE director = ?
ORDER BY rating DESC
LIMIT 1;
"""
DELETE_ALL_MOVIES = "DELETE FROM movies;"
DELETE_A_MOVIE = "DELETE FROM movies WHERE id = ?;"


def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection: 
    # saves interactions with the db file
        connection.execute(CREATE_MOVIES_TABLE)

def add_movie(connection, title, year, director, rating):
    with connection:
        connection.execute(INSERT_MOVIE, (title, year, director, rating))

def get_all_movies(connection):
    with connection:
        return connection.execute(GET_ALL_MOVIES).fetchall()

def get_top_movies(connection):
    with connection:
        return connection.execute(GET_TOP_MOVIES).fetchall()

def get_movies_by_name(connection, title):
    with connection:
        return connection.execute(GET_MOVIES_BY_TITLE, (title,)).fetchall()

def get_best_movie_of_director(connection, director):
    with connection:
        return connection.execute(GET_BEST_MOVIE_OF_DIRECTOR, (director,)).fetchone()

def delete_all_movies(connection):
    with connection:
        connection.execute(DELETE_ALL_MOVIES)

def delete_a_movie(connection, id):
    with connection:
        connection.execute(DELETE_A_MOVIE, (id,))