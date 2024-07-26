class Movie:

    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False
    
    def rent(self):
        if self.is_rented == True:
            print(f"Il film '{self.title}' è già noleggiato.")
        else:
            self.is_rented = True
    
    def return_movie(self):
        if self.is_rented == True:
            self.is_rented = False
            print(f"Il film '{self.title}' è già noleggiato.")
        else:
            print(f"Il film '{self.title}' non è attualmente noleggiato.")
    


class Customer:

    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = []
    
    def rent_movie(self, movie: Movie):
        if movie.is_rented == False:
            self.rented_movies.append(movie)
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")
    
    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
            print(f"Il film '{movie.title}' è già noleggiato.")
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")



class VideoRentalStore:

    def __init__(self) -> None:
        self.movies = {}
        self.customers = {}
    
    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movies:
            movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie
        else:
            print(f"Il film con ID {movie_id} esiste già.")
    
    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers:
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")
    
    def rent_movie(self, customer_id: str, movie_id: str):
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)
        if customer and movie:
            customer.rent_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str):
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)
        if customer and movie:
            customer.return_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str):
        customer = self.customers.get(customer_id)
        if customer:
            return customer.rented_movies
        else:
            print("Cliente non trovato.")
            return []


# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")


#Il film 'Inception' è già noleggiato.
#Il film 'Inception' non è stato noleggiato da questo cliente.
#Film noleggiati da Alice: []
#Film noleggiati da Bob: ['The Matrix']
