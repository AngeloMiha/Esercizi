class Specie:

    def __init__(self, nome: str, popolazione: int, tasso: float) -> None:
        self.nome: str = nome
        self.popolazione: int = popolazione
        self.tasso: float = tasso
    
    def cresci(self):
        self.popolazione: int = int(self.popolazione * (1 + self.tasso/100))
        return self.popolazione

    def anni_per_superare(self, altra_specie: 'Specie'):
        pass

    def getDensita(self, area_kmq: float):
        pass



class BufaloKlingon(Specie):

    def __init__(self, nome: str, popolazione: int, tasso: float, nome_ris: str) -> None:
        super().__init__(nome, popolazione, tasso)
        self.nome_ris: str = nome_ris



class Elefante(Specie):

    def __init__(self, nome: str, popolazione: int, tasso: float, nome_ris: str) -> None:
        super().__init__(nome, popolazione, tasso)
        self.nome_ris: str = nome_ris

