class Prodotto:

    def __init__(self, nome: str, quantita: int) -> None:
        self.nome: str = nome
        self.quantita: int = quantita



class Magazzino:

    def __init__(self) -> None:
        self.magazzino = []
    
    def aggiungi_prodotto(self, prodotto):
        self.magazzino.append(prodotto)
    
    def cerca_prodotto(self, prodotto):
        for prodotti in self.magazzino:
            if prodotti == prodotto:
                return f"Prodotto {prodotto} esistente."
        return f"Prodotto {prodotto} non esistente."
    
    def verifica_disponibilita(self, nome):
        for nome in self.magazzino:
            if Magazzino.cerca_prodotto(nome) and self.quantita > 0:
                return f"Prodotto {nome} disponibile."
        return f"Prodotto {nome} non disponibile."

prodotto1 = Prodotto("Prodotto A", 100)
prodotto2 = Prodotto("Prodotto B", 50)
prodotto3 = Prodotto("Prodotto C", 200)

# Creazione del magazzino
magazzino = Magazzino()

# Aggiunta dei prodotti al magazzino
magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
magazzino.aggiungi_prodotto(prodotto3)

# Ricerca di un prodotto
prodotto_trovato = magazzino.cerca_prodotto("Prodotto A")
print(prodotto_trovato)  # Output: Prodotto(nome="Prodotto A", quantità=100)

