from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name, last_name, cod_id: str):
        super().__init__(first_name, last_name)
        self.__cod_id = cod_id
    
    def setidCode(self, idCode):
        self.__cod_id = idCode
    
    def getidCode(self):
        return self.__cod_id
    
    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastname()} ID: {self.__cod_id}")
