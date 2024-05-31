class MovieCatalog:

    def __init__(self) -> None:
        self.catalogo: dict[str:set] = {}
    
    def add_movie(self, director_name: str, movies: set):
        self.catalogo[director_name] = movies

    def remove_movie(self, director_name: str, movie_name: str):
        self.catalogo[director_name] -= movie_name

    def list_directors(self):
        res: list = []
        for k in self.catalogo.keys():
            res.append(k)
        return res

    def get_movies_by_director(self, director_name: str):
        return self.catalogo[director_name]

    def search_movies_by_title(self, title: str):
        res: dict[str:set] = {}
        for k in self.catalogo.keys():
            for v in self.catalogo.values():
                if title == v:
                    res[k] = v
        return res



catalogo_film = MovieCatalog()

# Aggiungere alcuni film al catalogo
print(catalogo_film.add_movie("Christopher Nolan", ["Inception", "Interstellar", "Dunkirk"]))
print(catalogo_film.add_movie("Steven Spielberg", ["Jaws", "E.T.", "Jurassic Park"]))
print(catalogo_film.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill", "Django Unchained"]))

# Mostrare tutti i registi
print(catalogo_film.list_directors())

# Cercare i film di un regista specifico
print(catalogo_film.get_movies_by_director("Christopher Nolan"))

# Rimuovere un film dal catalogo
print(catalogo_film.remove_movie("Christopher Nolan", "Dunkirk"))

# Cercare un film per titolo
print(catalogo_film.search_movies_by_title("Park"))

# Mostrare i film di un regista dopo la rimozione di un film
print(catalogo_film.get_movies_by_director("Christopher Nolan"))
