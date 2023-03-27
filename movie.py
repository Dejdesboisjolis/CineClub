import json 
import logging
import os

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR,"data","movies.json")

def get_movies():
    movies = []
    with open(DATA_FILE,"r") as f:
        movies_title = json.load(f)
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


class Movie:
    def __init__(self,title):
        self.title = title
    
    def __str__(self) -> str:
        return self.title
    
    def _get_movies(self):
        with open(DATA_FILE,"r") as f:
            return json.load(f)

    def _write_movies(self,movies):
        with open("data/movies.json","w") as f:
            json.dump(movies,f,indent = 4)

    def add_to_movies(self):
        """Ajout d'un film

        Resume : 
        Je parcours la liste des films
        Je verifie que mon film ne soit pas present dans la liste 
        Si ce n'est pas le cas je l'ajoute
        """
        movies = self._get_movies()
        if  not self.title in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est deja dans la liste")
            return False
        
    def delete_to_movies(self):
        movies = self._get_movies()

        if not self.title in movies:
            logging.warning(f"Le film {self.title} n'est pas dans la liste")
            return False
        else:
            movies.remove(self.title)
            self._write_movies(movies)
            return True




    
    


m = Movie("Booba le retour ")
print(m)
m._write_movies(["Le silence des agneaux","La verite si je bande"])
m.add_to_movies()
print(Movie._get_movies(m))
m.add_to_movies()
m.delete_to_movies()
print(Movie._get_movies(m))
m.delete_to_movies()
print(get_movies())