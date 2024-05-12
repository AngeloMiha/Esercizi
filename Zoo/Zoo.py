class Zoo:
    def __init__(self):
        self.fences = []
        self.zoo_keepers = []
    
    def describe_zoo(self):
        print("Guardians:\n")
        for keeper in self.zoo_keepers:
            print(f"ZooKeeper(name={keeper.name}, surname={keeper.surname}, id: {keeper.id})\n")

        print("Fences:\n")
        for fence in self.fences:
            if fence.animals:
                print(f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})\n")
                print("With animals:\n")
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})\n")
                print("#" * 30, "\n")
            else:
                print(f"There's no animal in this fence={fence.habitat}")
    
    def add_fence(self, fence):
        self.fences.append(fence)
    
    def add_keeper(self, keeper):
        self.zoo_keepers.append(keeper)



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
        self.animals.append(animal)
    
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} removed from the {self.habitat} Fence.")
            self.area += (animal.height * animal.width)
        else:
            print(f"{animal.name} is not in the {self.habitat} Fence.")


class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(animal, fence):
        if animal.preferred_habitat == fence.habitat and fence.area >= (animal.height * animal.width):
            fence.add_animal(animal)
            print(f"You've add {animal.name} ({animal.species}) at the {fence.habitat} Fence.")
        else:
            print(f"Impossible to add {animal.name} ({animal.species}) at the {fence.habitat} Fence.")
    
    def remove_animal(animal, fence):
        if animal in fence.animals:
            fence.remove_animal(animal)
            print(f"You've removed {animal.name} ({animal.species}) from the {fence.habitat} Fence.")
            fence.area += (animal.height * animal.width)
        else:
            print(f"{animal.name} ({animal.species}) is not in the {fence.habitat} Fence.")
    
    def feed(animal, fence):
        if animal in Fence[animal.preferred_habitat].animals:
            if (animal.height * 1.02) * (animal.width * 1.02) <= Fence.area:
                animal.health += 1
                animal.height *= 1.02
                animal.width *= 1.02
                print(f"{ZooKeeper.name} {ZooKeeper.surname} has feed {animal.name} ({animal.species}). {animal.name}'s health is at {animal.health}%")
            else:
                print(f"There's not enough space to feed {animal.name} ({animal.species}).")
        else:
            print(f"{animal.name} ({animal.species}) isn't in the {animal.preferred_habitat} Fence.")

    def clean(fence):
        area_occupied = sum(animal.height * animal.width for animal in fence.animals)
        area_remaining = fence.area - area_occupied
        if area_remaining > 0:
            cleaning_time = area_occupied / area_remaining
        else:
            cleaning_time = area_occupied
        print(f"{ZooKeeper.name} {ZooKeeper.surname} has cleaned the {fence.habitat} Fence. Time spent: {cleaning_time} hours.")
        return cleaning_time
