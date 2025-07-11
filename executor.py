# executor.py
from PyQt5 import QtWidgets
from PyQt5.QtChart import QChart, QPieSeries
from movies import Ui_MainWindow
from movielogics import Database
from movietuple import TupledMovie

class Execute(QtWidgets.QMainWindow):
    def __init__(self, database):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Setup UI correctly

        self.database = database
        self.upload_films()
        
        self.ui.insert_button.clicked.connect(self.add_film)
        self.ui.update_button.clicked.connect(self.update_film)
        self.ui.delete_button.clicked.connect(self.delete_film)
        self.ui.compare_button.clicked.connect(self.add_pie_chart)

    def upload_films(self):
        self.films = self.database.select_movies()
        self.ui.listWidget.clear()
        for film in self.films:
            self.ui.listWidget.addItem(f"{film.id}: {film.name} ({film.year}),audience:{film.movie_rated},"
                                       f"rating:{film.rating},raters:{film.num_raters},reviews:{film.num_reviews}")

    def add_film(self):
        try:
            film = TupledMovie(
                None,
                self.ui.name_lineEdit.text(),
                float(self.ui.year_lineEdit.text()),
                self.ui.audience_lineEdit.text(),
                float(self.ui.rating_lineEdit.text()),
                int(self.ui.raters_lineEdit.text()),
                int(self.ui.reviews_lineEdit.text())
            )
            self.database.insert_movies(film)
            self.upload_films()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "შეცდომა", f"მონაცემების დამატებისას მოხდა შეცდომა:\n{e}")

    def update_film(self):
        try:
            film = TupledMovie(
                None,
                self.ui.name_lineEdit.text(),
                None,
                None,
                float(self.ui.rating_lineEdit.text()),
                None,
                None
            )
            self.database.update_movies(film)
            self.upload_films()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "შეცდომა", f"მონაცემების განახლებისას მოხდა შეცდომა:\n{e}")

    def delete_film(self):
        try:
            rating = float(self.ui.rating_lineEdit.text())
            self.database.delete_movies(rating)
            self.upload_films()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "შეცდომა", f"მონაცემების წაშლისას მოხდა შეცდომა:\n{e}")

    def add_pie_chart(self):
        category1 = self.ui.audition_lineEdit_1.text().strip()
        category2 = self.ui.audition_lineEdit_2.text().strip()

        if not category1 or not category2:
            QtWidgets.QMessageBox.warning(self, "შეცდომა", "გთხოვთ შეიყვანეთ ორივე აუდიტორიის ტიპი.")
            return None

        count1 = self.database.count_rated_movie(category1)
        count2 = self.database.count_rated_movie(category2)

        total = count1 + count2
        if total == 0:
            QtWidgets.QMessageBox.information(self, "ინფორმაცია", "მონაცემები ვერ მოიძებნა მითითებული აუდიტორიებისთვის.")
            return

        series = QPieSeries()
        slice1 = series.append(category1, count1)
        slice2 = series.append(category2, count2)

        slice1.setLabel(f"{category1} - {count1} ({count1 / total * 100:.1f}%)")
        slice2.setLabel(f"{category2} - {count2} ({count2 / total * 100:.1f}%)")

        slice1.setLabelVisible(True)
        slice2.setLabelVisible(True)

        chart = QChart()
        chart.setTitle("აუდიენციის მიხედვით შეფასება (%)")
        chart.addSeries(series)

        self.ui.pie_chart.setChart(chart)
