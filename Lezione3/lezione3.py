# Number 4 - 1
print("Number 4-1:")
pizzas: list[str] = ["margherita", "crostino", "diavola"]
i: int = 1
for pizza in pizzas:
    print("Pizza number", i, "is", pizza)
    i += 1
i = 0
print("I really like", pizzas[i], "pizza !!! ")
i += 1
print("I really like", pizzas[i], "pizza !!! ")
i += 1
print("I really like", pizzas[i], "pizza !!! ")


# Number 4 - 2
print("\n")
print("Number 4-2:")
animals: list[str] = ["monkey", "tiger", "cat"]
i: int = 1
for animal in animals:
    print("Animal number", i, "is", animal)
    i += 1
i = 0
print("The", animals[i], "is my faourite animal")
i += 1
print("The", animals[i], "is the king of the jungle")
i += 1
print("I'm allergic to a", animals[i])
print("All this animals are my favourite !!")


# Number 4 - 3
print("\n")
print("Number 4-3:")
num: int = 1
for i in range(20):
    print(num, " ")
    num += 1


# Number 4 - 4
print("\n")
print("Number 4-4:")
l: list[float] = []
num: int = 1
for i in range(10):
    l.append(num)
    num += 1

print(l)
