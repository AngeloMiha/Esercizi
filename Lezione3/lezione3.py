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


# Number 4 - 5
print("\n")
print("Number 4-5:")
print("Min number:", min(l), "\n"
      "Max number:", max(l))
print("Sum numbers:", sum(l))


# Number 4 - 6
print("\n")
print("Number 4-6:")
num: int = 1
for i in range(20):
    if num % 2 != 0:
        print(num)
        num += 1
    else:
        num += 1
        continue


# Number 4 -7
print("\n")
print("Number 4-7:")
multiples_of_three: list[float] = []
for i in range(3, 33, 3):
    multiples_of_three.append(i)
print(multiples_of_three)


# Number 4 - 8
print("\n")
print("Number 4-8:")
power: list[float] = []
for num in range(1, 11, 1):
    power.append(num ** 3)
print(power)


# Number 4 - 9
print("\n")
print("Number 4-9:")
power: list[float] = [num ** 3 for num in range(1, 11)]
print(power)


# Number 4 - 10
print("\n")
print("Number 4-10:")
power: list[float] = [num ** 3 for num in range(1, 11)]
print(power)
print("First:", power[:3])
middle = len(power) // 2
print("Middle:", power[middle - 1:middle + 2])
print("Last:", power[-3:])


