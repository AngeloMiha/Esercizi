class Media:
    def __init__(self, title) -> None:
        self.title: str = title
        self.reviews: list[int] = []
    
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title
    
    def agg_val(self, voto):
        self.reviews.append(voto)
    
    def get_media(self):
        if not self.reviews:
            return 0
        media: float = sum(self.reviews) / len(self.reviews)
        return media
    
    def get_rate(self):
        media = self.get_media()
        if media <= 1.4:
            return "Terribile"
        elif 1.5 <= media <= 2.4:
            return "Brutto"
        elif 2.5 <= media <= 3.4:
            return "Normale"
        elif 3.5 <= media <= 4.4:
            return "Bello"
        elif 4.5 <= media <= 5:
            return "Grandioso"

    def rate_percent(self, voto):
        if not self.reviews:
            return 0
        i: int = self.reviews.count(voto)
        return (i / len(self.reviews)) * 100

    def recensione(self):
        return (
            f"Titolo del Film: {self.get_title()} \n"
            f"Voto Medio: {self.get_media():.2f} \n"
            f"Giudizio: {self.get_rate()} \n"
            f"Terribile: {self.rate_percent(1):.2f}% \n"
            f"Brutto: {self.rate_percent(2):.2f}% \n"
            f"Normale: {self.rate_percent(3):.2f}% \n"
            f"Bello: {self.rate_percent(4):.2f}% \n"
            f"Grandioso: {self.rate_percent(5):.2f}%"
        )


film1 = Media("Il Mio Film")
film1.agg_val(5)
film1.agg_val(3)
film1.agg_val(4)

film2 = Media("Il Tuo Film")
film2.agg_val(3)
film2.agg_val(2)
film2.agg_val(1)

print(film1.recensione())
print("\n")
print(film2.recensione())
