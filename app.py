import sys
from PySide2 import QtWidgets,QtCore
from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.setWindowTitle('CineClub')
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        # Création des widgets
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovie = QtWidgets.QPushButton("Supprimer le(s) films(s)")

        # Ajout des widgets au layout

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovie)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovie.clicked.connect(self.remove_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)



    def populate_movies(self):
        movies = get_movies()

        for mov in movies :
            #methode 1
            #self.lw_movies.addItem(mov.title)
            #methode 2
            lw_item = QtWidgets.QListWidgetItem(mov.title)
            lw_item.setData(QtCore.Qt.UserRole,mov)
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        print("film ajouté")
        """
        Recuperer le texte dans le line edit
        Creer une instance Movie
        Ajouter le film dans le fichier json
        Ajouter le titre du film dans le list widget
        """
        texte_from_lineEdit = self.le_movieTitle.text()
        if not texte_from_lineEdit:
            return False
        movie_from_texte = Movie(title=texte_from_lineEdit)

        if movie_from_texte.add_to_movies():
            lw_item = QtWidgets.QListWidgetItem(movie_from_texte.title)
            lw_item.setData(QtCore.Qt.UserRole,movie_from_texte)
            self.lw_movies.addItem(lw_item)
            self.le_movieTitle.setText("")
    
    def remove_movie(self):

        for select_item in self.lw_movies.selectedItems():
            movie = select_item.data(QtCore.Qt.UserRole)
            movie.delete_to_movies()
            self.lw_movies.takeItem(self.lw_movies.row(select_item))


# Création de l'application
app = QtWidgets.QApplication([])

# Création de la fenêtre principale
window = App()
window.show()

# Lancement de l'application
app.exec_()
