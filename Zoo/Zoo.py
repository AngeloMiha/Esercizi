class Zoo:
    def __init__(self, fences = [], zoo_keepers = []) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers



class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, health: float) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.widht = width
        self.preferred_habitat = preferred_habitat
        self.health = health

        def area_animal(self):
            return height * width



class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area = area
        self.temperature = temperature
        self.habitat = habitat



class ZooKeeper:
    def __init__(self, name, surname, id) -> None:
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal):
        if Animal.preferred_habitat == Fence.habitat and Animal.height*Animal.widht <= Fence.area:
            self.animals.append(animal)
        else:
            pass




tiger: Animal = Animal(name = "Tiger", height = "5", width = "5", preferred_habitat = "sus")
savana: Fence = Fence(area = 200, habitat = "sus")

