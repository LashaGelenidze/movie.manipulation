from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView, QChart, QPieSeries
from movietuple import TupledMovie

from movies import Ui_MainWindow

class Execute(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,database):
        super().__init__()
        self.database=database
        self.insert_button.clicked.connect(self.add_film())
        self.update_button.clicked.connect(self.update_film())
        self.delete_button.clicked.connect(self.delete_film())
        self.compare_button.clicked.connect(self.add_pie_chart())
        self.upload_films

    def upload_films(self):
        self.films = self.database.select_movies()
        self.ListWidget.clear()
        for film in self.films:
            self.ListWidget.addItem(f"{film.id}: {film}")

    def add_film(self):
        film = TupledMovie(None,self.name_lineEdit, int(self.year_lineEdit),
                           self.audience_lineEdit, float(self.rating_lineEdit), int(self.raters_lineEdit), int(self.reviews_lineEdit))
        self.database.insert_movies(film)
        self.upload_films()

    def update_film(self):
        self.database.update_movies(float(self.rating_lineEdit),self.name_lineEdit)
        self.upload_films()

    def delete_film(self):
        self.database.delete_movies(float(self.rating_lineEdit))
        self.upload_films()
        
    @ staticmethod
    def count_rated_movie(cursor,for_audience):
        return cursor.execute("SELECT count(*) FROM movies WHERE movie_rated=?", (for_audience,)).fetchone()[0]

    def add_pie_chart(self):
        self.pie_chart=QChart()
        self.pie_chart.setTitle("აუდიენციის მიხედვით შეფასება")
        first=Database.count_rated_movie(self.cursor, self.audition_lineEdit_1)
        second = Database.count_rated_movie(self.cursor, self.audition_lineEdit_2)

        self.series = QPieSeries()
        self.series.append(f"{self.audition_lineEdit_1}", first)
        self.series.append(f"{self.audition_lineEdit_2}", second)
        self.pie_chart.addSeries(self.series)
        self.chart_view.setChart(self.pie_chart)


