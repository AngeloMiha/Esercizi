class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def __str__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"
    
    def talk(self):
        return "Non so come si parla..."



class Person(Animal):

    def talk(self):
        return f"Ciao, mi chiamo {self.name}"

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"
    
    def __add__(self, other):
        return Person(name=self.name + other.name, age=self.age + other.age)
    
    def __eq__(self, other) -> bool:
        return self.name == other.name
    


class Studente(Person):

    def __init__(self, name, age, id) -> None:
        s = super().__init__(name, age)
        self.id = id

    def talk(self):
        return f"Ciao sono uno studente e mi chiamo {self.name}"
    
    def bella(self, new):
        super().set_age(new)
    


p = Person(name="sis", age=23)
p1 = Person(name="sus", age=21)

p2 = p + p1
print(p2)

print(p == p1)
print(p != p1)
