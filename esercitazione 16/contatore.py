class Contatore:

    def __init__(self) -> None:
        self.conteggio = 0

    def setZero(self):
        self.conteggio = 0

    def add1(self):
        self.conteggio += 1

    def sub1(self):
        if self.conteggio >= 1:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
    
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print("Conteggio attuale: {self.conteggio}")