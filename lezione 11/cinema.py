class Film:

    def __init__(self, titolo: str, durata: float) -> None:
        self.titolo: str = titolo
        self.durata: float = durata



class Sala:

    def __init__(self, id_sala: str, film: str, posti_tot: int) -> None:
        self.id_sala: str = id_sala
        self.film: str = film
        self.posti_tot: int = posti_tot
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti: int):
        if self.posti_disponibili() >= num_posti:
            self.posti_prenotati += num_posti
            return f"Hai prenotato {num_posti} posti."
        else:
            return f"Non ci sono {num_posti} posti disponibili."

    def posti_disponibili(self):
        posti_dis: int = self.posti_tot - self.posti_prenotati
        return posti_dis



class Cinema:

    def __init__(self) -> None:
        self.sale = []

    def aggiungi_sala(self, sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int):
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return f"Non esiste questo film."
