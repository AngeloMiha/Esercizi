class Media:

    def __init__(self, title) -> None:
        self.title: str = title
        self.reviews: list[int] = []
    
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return f"Titolo media: {self.title}"
    
    def agg_val(self, voto):
        return self.reviews.append(voto)
    
    def get_media(self):
        media: float = 0
        for num in self.reviews:
            media += num
        return media / len(self.reviews)
    
    def get_rate(self):
        if self.get_rate <= 1.4:
            return f"Terribile"
        elif 1.5 <= self.get_media <= 2.4:
            return f"Brutto"
        elif 2.5 <= self.get_media <= 3.4:
            return f"Normale"
        elif 3.5 <= self.get_media <= 4.4:
            return f"Bello"
        elif 4.5 <= self.get_media <= 5:
            return f"Grandioso"

    def rate_percent(self, voto):
        i: int = self.reviews.count(voto)
        return (i / len(self.reviews)) *  100

    def recensione(self):
        return f"Titolo del Film: {self.get_title} \n Voto Medio: {self.get_media} \n Giudizio: {self.get_rate} \n 
        Terribile: {self.rate_percent(1)} \n Brutto: {self.rate_percent(2)} \n Normale: {self.rate_percent(3)} \n 
        Bello: {self.rate_percent(4)} \n Grandioso: {self.rate_percent(5)}"



