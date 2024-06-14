from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name, last_name, spec: str, parc: float):
        super().__init__(first_name, last_name)
        
        if isinstance(spec, str):
            self.__spec = spec
        else:
            self.__spec = None
            print("La specializzazione inserita non è una stringa!")
        
        if isinstance(parc, float):
            self.__parc = parc
        else:
            self.__parc = None
            print("La parcella inserita non è un float!")

    def setSpec(self, spec):
        if isinstance(spec, str):
            self.__spec = spec
        else:
            print("La specializzazione inserita non è una stringa!")
    
    def setParc(self, parc):
        if isinstance(parc, float):
            self.__parc = parc
        else:
            print("La parcella inserita non è un float!")
    
    def getSpec(self):
        return self.__spec
    
    def getParc(self):
        return self.__parc
    
    def isAValidDoctor(self):
        age = self.getAge()
        if age is not None and age > 30:
            print(f"Doctor {self.getName()} {self.getLastname()} is valid!")
        else:
            print(f"Doctor {self.getName()} {self.getLastname()} is not valid!")
    
    def doctorGreet(self):
        self.greet()
        if self.__spec is not None:
            print(f"Sono un medico {self.__spec}")
        else:
            print("Specializzazione non disponibile.")
