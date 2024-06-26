class Film:

    def __init__(self,id: int, title: str) -> None:
        self.__id: int =id
        self.__title: str = title

    def setID(self, id: int):
        self.__id = id
        return self.__id
    
    def setTitle(self, title: str):
        self.__title = title
        return self.__title
    
    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def isEqual(self, otherFilm: int):
        if self.getID == otherFilm:
            return True
        return False
