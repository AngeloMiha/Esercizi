class Libro:

    def __init__(self, titolo: str, autore: str) -> None:
        self.titolo: str = titolo
        self.autore: str = autore
        self.stato_pre: bool = True



class Biblioteca:

    def __init__(self) -> None:
        self.biblioteca = []

    def aggiungi_libro(self, libro):
        self.biblioteca.append(libro)
        return f"Hai aggiunto {libro} nella biblioteca."

    def presta_libro(self, titolo_libro):
        for libro in self.biblioteca:
            if libro.titolo == titolo_libro and libro.stato_pre == True:
                libro.stato_pre = False
                return f"Il libro {titolo_libro} è disponibile."
        return f"Il libro {titolo_libro} non è disponibile."

    def restituisci_libro(self, titolo_libro):
        for libro in self.biblioteca:
            if libro.titolo == titolo_libro and libro.stato_pre == False:
                libro.stato_pre = True
                return f"Il libro {titolo_libro} ora è disponibile."
        return f"Il libro {titolo_libro} è già disponibile."

    def mostra_libri_disponibili(self):
        i = 0
        for libro in self.biblioteca:
            if libro.stato_pre == True:
                print(f"Il libro {libro} è disponibile.")
                i += 1
        if i == 0:
            return f"Non ci sono libri disponibili."



biblioteca = Biblioteca()

# Aggiungere alcuni libri al catalogo
biblioteca.aggiungi_libro(Libro("Il Nome della Rosa", "Umberto Eco"))
biblioteca.aggiungi_libro(Libro("1984", "George Orwell"))
biblioteca.aggiungi_libro(Libro("Moby Dick", "Herman Melville"))

# Mostrare i libri disponibili
print(biblioteca.mostra_libri_disponibili())

# Prestare un libro
print(biblioteca.presta_libro("1984"))

# Mostrare i libri disponibili dopo il prestito
print(biblioteca.mostra_libri_disponibili())

# Restituire un libro
print(biblioteca.restituisci_libro("1984"))

# Mostrare i libri disponibili dopo la restituzione
print(biblioteca.mostra_libri_disponibili())