class Documento:

    def __init__(self, text: str) -> None:
        self.text: str = text
    
    def setText(self, new_text: str):
        self.text = new_text
    
    def getText(self):
        return self.text
    
    def isInText(self, key_word):
        if key_word in self.text:
            return True
        return False
    


class Email(Documento):

    def __init__(self, text: str, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(text)
        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo: str = titolo
    
    def set(self, mittente: str):
        self.mittente = mittente

    def set(self, destinatario: str):
        self.destinatario = destinatario

    def set(self, titolo: str):
        self.titolo = titolo

    def getM(self):
        return self.mittente

    def getD(self):
        return self.destinatario

    def getT(self):
        return self.titolo

    def getText(self):
        print(f"Da: {self.getM()}, A: {self.getD()} \n Titolo: {self.getT()} \n Messaggio: {self.text}")
    
    def writeToFile(self):
        pass



class File(Documento):

    def __init__(self, text: str, nomePercorso: str) -> None:
        super().__init__(text)
        self.nomePercorso:str = nomePercorso
    
    