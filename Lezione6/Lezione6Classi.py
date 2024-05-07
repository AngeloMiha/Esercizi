'''
class Person:
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name: int = name 
        self.age: int = age
        self.height: int = height
        self.weight: int = weight
        self.hobby: list[str] = []
    
    def bulk_set_hobby(self, new_hobbies: list[str]):
        self.hobby = self.hobby.union(set(new_hobbies))

    def set_hobby(self, new_hobby: str):
        self.hobby.append(new_hobby)
        # self.hobby.union(set([new_hobby]))

    def remove_hobby(self, old_hobby: str):
        if old_hobby in self.hobby:
            self.hobby.remove(old_hobby)

alice: Person = Person("Alice W.", 45, 150, 10)
bob: Person = Person("Bob M.", 36, 180, 7)
mattia: Person = Person("Mattia Rò.", 7, 170, 9)
angelo: Person = Person("Angelo M.", 19, 195, 6)
mamma: Person = Person("Mamma Sus.", 28, 200, 5)

oldest: str = ""
if alice.age > bob.age:
    oldest = alice.name
else:
    oldest = bob.name
print(oldest)


people: list[Person] = [alice, bob, mattia, angelo, mamma]
youngest_age: int = alice.age
youngest_name: str = ""
for i in people:
    if i.age < youngest_age:
        youngest_name = i.name
        youngest_age = i.age
    else:
        continue
print("Nome:", youngest_name, "Età:", youngest_age)


alice.set_hobby("Basket")
bob.set_hobby("Calcio")
mattia.set_hobby("Nuoto")
angelo.set_hobby("Pallavolo")
mamma.set_hobby("Karate")
'''

'''
class Student:
    def __init__(self, name: str, studyProgram: str) -> None:
        self.name = name
        self.studyProgram = studyProgram
        self.age = None
        self.gender = None

    def __str__(self) -> str:
        if self.age and self.gender:
            return f"Name:{self.name}, StudyProgram:{self.studyProgram}, age:{self.age}, gender:{self.gender})"
        else:
            if self.age:
                return f"Name:{self.name}, StudyProgram:{self.studyProgram}, age:{self.age})"
            elif self.gender:
                return f"Name:{self.name}, StudyProgram:{self.studyProgram} gender:{self.gender})"
            else:
                return f"Name:{self.name}, StudyProgram:{self.studyProgram})"
            
    def printInfo(self):
        return self.__str__()

    def set_age(self, new_age: int):
        self.age: int = new_age

    def set_gender(self, new_gender: str):
        self.gender: str = new_gender


myself: Student = Student("Angelo", "Python")
left: Student = Student("Mamma", "Java")
right: Student = Student("Mattia", "c++")

print(myself.printInfo())
print(left.printInfo())
print(right.printInfo())

myself.set_age(19)
left.set_age(32)
right.set_age(4)

myself.set_gender("Male")
left.set_gender("NonBinary")
right.set_gender("Female")

print(myself.printInfo())
print(left.printInfo())
print(right.printInfo())
'''

'''
class Animal:
    def __init__(self, name: str, legs: int) -> None:
        self.name = name
        self.legs = legs

    def __str__(self) -> str:
        return f"Name:{self.name}, legs:{self.legs}"
    
    def printInfo(self):
        return self.__str__()
    
    def printName(self):
        return f"Name:{self.name}"

    def set_legs(self, new_legs: int):
        self.legs: int = new_legs

    def get_legs(self):
        return f"Legs : {self.legs}"

dog = Animal(name = "dog", legs = 4)
cat = Animal(legs = 4, name = "cat")

print(dog.printName())
print(cat.printName(), "\n")

dog.legs = 1
print(dog.get_legs(), "\n")

dog.set_legs(2)
cat.set_legs(5)
print(dog.get_legs())
print(cat.get_legs(), "\n")

print(dog.printInfo())
print(cat.printInfo())
'''