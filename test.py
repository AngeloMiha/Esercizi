import math

class Zoo:
    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

    def add_fence(self, fence):
        self.fences.append(fence)

    def add_zoo_keeper(self, zoo_keeper):
        self.zoo_keepers.append(zoo_keeper)

    def describe_zoo(self):
        print("Zoo Keepers:")
        for keeper in self.zoo_keepers:
            print(f"{keeper.name} {keeper.surname} - ID: {keeper.id}")

        print("\nFences:")
        for fence in self.fences:
            print(f"Fence Area: {fence.area}, Temperature: {fence.temperature}, Habitat: {fence.habitat}")
            print("Animals:")
            for animal in fence.animals:
                print(f"Name: {animal.name}, Species: {animal.species}, Age: {animal.age}, Health: {animal.health}")

class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)

class Fence:
    def __init__(self, area, temperature, habitat):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def add_animal(self, animal):
        if self.area >= animal.height * animal.width and animal.preferred_habitat == self.habitat:
            self.area -= animal.height * animal.width
            self.animals.append(animal)
            print(f"{animal.name} added to the fence.")
        else:
            print(f"{animal.name} cannot be added to this fence.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.area += animal.height * animal.width
            self.animals.remove(animal)
            print(f"{animal.name} removed from the fence.")
        else:
            print(f"{animal.name} is not in this fence.")

class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def feed(self, animal, fence):
        if animal.health < 100 and animal.height * animal.width <= fence.area:
            animal.health += 1
            animal.height *= 1.02
            animal.width *= 1.02
            print(f"{self.name} fed {animal.name}.")
        else:
            print(f"{self.name} cannot feed {animal.name}.")

    def clean(self, fence):
        occupied_area = sum(animal.height * animal.width for animal in fence.animals)
        if fence.area - occupied_area > 0:
            cleaning_time = occupied_area / (fence.area - occupied_area)
        else:
            cleaning_time = occupied_area
        print(f"{self.name} cleaned the fence. Cleaning time: {cleaning_time}")


# Esempio di utilizzo:

zoo = Zoo()

fence1 = Fence(area=1000, temperature="Warm", habitat="Savannah")
fence2 = Fence(area=500, temperature="Cold", habitat="Arctic")

zoo.add_fence(fence1)
zoo.add_fence(fence2)

zoo_keeper1 = ZooKeeper(name="John", surname="Doe", id="123")
zoo_keeper2 = ZooKeeper(name="Jane", surname="Smith", id="456")

zoo.add_zoo_keeper(zoo_keeper1)
zoo.add_zoo_keeper(zoo_keeper2)

lion = Animal(name="Simba", species="Lion", age=5, height=2, width=3, preferred_habitat="Savannah")
penguin = Animal(name="Penny", species="Penguin", age=2, height=1, width=1, preferred_habitat="Arctic")

fence1.add_animal(lion)
fence2.add_animal(penguin)

zoo_keeper1.feed(lion, fence1)
zoo_keeper2.clean(fence1)

zoo.describe_zoo()
