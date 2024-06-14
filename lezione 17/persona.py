class Persona:

    def __init__(self, first_name: str, last_name: str) -> None:
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è una stringa!")
            
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print("Il cognome inserito non è una stringa!")

        if isinstance(first_name, str) and isinstance(last_name, str):
            self.__age = 0
        else:
            self.__age = None

    def setName(self, first_name: str):
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")
    
    def setLastName(self, last_name: str):
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")
    
    def setAge(self, age: int):
        if isinstance(age, int):
            self.__age = age
        else:
            print("L'età deve essere un numero intero!")
    
    def getName(self):
        return f"Nome: {self.__first_name}."
    
    def getLastname(self):
        return f"Cognome: {self.__last_name}."
    
    def getAge(self):
        return f"Nome: {self.__age}."
    
    def greet(self):
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")
    
