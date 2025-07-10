from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView, QChart, QPieSeries
from movietuple import TupledMovie

from movies import Ui_MainWindow

class Execute(Ui_MainWindow):
    def __init__(self,database):
        super().__init__()
        self.database=database
        self.insert_button.clicked.connect(self.add_film())
        self.update_button.clicked.connect(self.update_film())
        self.delete_button.clicked.connect(self.delete_film())
        self.upload_films

    def upload_films(self):
        self.films = self.database.select_movies()
        self.ListWidget.clear()
        for film in self.films:
            self.ListWidget.addItem(f"{film.id}: {film}")

    def add_film(self):
        film = TupledMovie(None,self.name_lineEdit, int(self.year_lineEdit),
                           self.audience_lineEdit, float(self.rating_lineEdit), int(self.raters_lineEdit), int(self.reviews_lineEdit))
        self.db.insert_movies(film)
        self.upload_films()

    def update_film(self):
        film = TupledMovie(float(self.rating_lineEdit),self.name_lineEdit)
        self.db.update_movies(film)
        self.upload_films()

    def delete_film(self):
        self.db.delete_movies(float(self.rating_lineEdit))
        self.load_books()


