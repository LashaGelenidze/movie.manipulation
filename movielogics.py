import sqlite3
from movietuple import TupledMovie
from PyQt5.QtChart import QChart, QChartView, QPieSeries
class Database:
    def __init__(self, db_name="movie.sqlite3"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year REAL NOT NULL,
                movie_rated TEXT NOT NULL,
                rating REAL NOT NULL,
                num_raters REAL NOT NULL,
                num_reviews REAL NOT NULL
            )
        """)
        self.conn.commit()

    def select_movies(self):
        self.cursor.execute("SELECT * FROM movies")
        lines=self.cursor.fetchall()
        return [TupledMovie(*line) for line in lines]

    def insert_movies(self,film):
        self.cursor.execute("INSERT INTO movies (name,year,movie_rated,rating,num_raters,num_reviews) VALUES (?, ?, ?)",
                            film.tupled())
        self.conn.commit()

    def update_movies(self, film):
        self.cursor.execute("UPDATE movies SET rating=? WHERE name=?",
                            (film.rating, film.name))
        self.conn.commit()

    def delete_movies(self, rating):
        self.cursor.execute("DELETE FROM movies WHERE rating=?", (rating, ))
        self.conn.commit()

