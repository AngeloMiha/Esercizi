from film import Film

class Azione(Film):
    
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = "Azione"
        self.__penale: int = 3
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaRitardoPenale(self):
        pass



class Commedia(Film):
    
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = "Commedia"
        self.__penale: int = 2,50

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaRitardoPenale(self):
        pass



class Drama(Film):
    
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = "Drammatico"
        self.__penale: int = 2
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaRitardoPenale(self):
        pass
