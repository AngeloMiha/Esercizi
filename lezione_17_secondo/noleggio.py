from film import Film

class Noleggio:

    def __init__(self, film_list: list[Film]) -> None:
        self.film_list: list[Film] = film_list
        self.rented_film: dict = {}
    
    def isAvaible(self, film: Film):
        for cont in self.film_list:
            if cont.getTitle() == film.getTitle():
                print(f"Il film scelto è disponibile: {film.getTitle}!")
                return True
            print(f"Il film scelto non è disponibile: {film.getTitle}!")
            return False
    
    def rentAMovie(self, film: Film, clientID: int):
        pass

