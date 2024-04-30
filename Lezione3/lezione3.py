import random

# 4-1. Pizzas
print("Number 4-1:")
pizzas: list[str] = ["margherita", "rossa", "diavola"]
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


# 4-2. Animals
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


# 4-3. Counting to Twenty
print("\n")
print("Number 4-3:")
num: int = 1
for i in range(20):
    print(num, " ")
    num += 1


# 4-4. One Million
print("\n")
print("Number 4-4:")
l: list[float] = []
num: int = 1
for i in range(10):
    l.append(num)
    num += 1

print(l)


# 4-5. Summing a Million
print("\n")
print("Number 4-5:")
print("Min number:", min(l), "\n"
      "Max number:", max(l))
print("Sum numbers:", sum(l))


# 4-6. Odd Numbers
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


# 4-7. Threes
print("\n")
print("Number 4-7:")
multiples_of_three: list[float] = []
for i in range(3, 33, 3):
    multiples_of_three.append(i)
print(multiples_of_three)


# 4-8. Cubes
print("\n")
print("Number 4-8:")
power: list[float] = []
for num in range(1, 11, 1):
    power.append(num ** 3)
print(power)


# 4-9. Cube Comprehension
print("\n")
print("Number 4-9:")
power: list[float] = [num ** 3 for num in range(1, 11)]
print(power)


# 4-10. Slices
print("\n")
print("Number 4-10:")
power: list[float] = [num ** 3 for num in range(1, 11)]
print(power)
print("First:", power[:3])
middle = len(power) // 2
print("Middle:", power[middle - 1:middle + 2])
print("Last:", power[-3:])


# 4-11. My Pizzas, Your Pizzas
print("\n")
print("Number 4-11:")
friend_pizzas: list[str] = ["bufala", "crostino", "bianca"]
pizzas.append("rustica")
friend_pizzas.append("marinara")
print("My favourite pizzas are:", pizzas)
print("My friend's favourite pizzas are: ", friend_pizzas)


# 4-12. More Loops
print("\n")
print("Number 4-12:")
print("My pizzas:")
for pizza in pizzas:
    print(pizza)
print("My friend's pizzas:")
for pizza in friend_pizzas:
    print(pizza)


# 5-1. Conditional Tests
print("\n")
print("Number 5-1:")
car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs car != 'honda'? I predict True.")
print(car != 'honda')
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')
print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')
print("\nIs car.startswith('s')? I predict True.")
print(car.startswith('s'))
print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)
print("\nIs 'u' in car? I predict True.")
print('u' in car)
print("\nIs 'e' in car? I predict False.")
print('e' in car)
print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

# 5-2. More Conditional Tests
print("\n")
print("Number 5-2:")
name = 'John'
age = 25
numbers = [1, 2, 3, 4, 5]

print("Test 1: Is name == 'John'? I predict True.")
print(name == 'John')
print("\nTest 2: Is name == 'john'? I predict False.")
print(name == 'john')
print("\nTest 3: Is name.lower() == 'john'? I predict True.")
print(name.lower() == 'john')
print("\nTest 4: Is age == 25? I predict True.")
print(age == 25)
print("\nTest 5: Is age != 30? I predict True.")
print(age != 30)
print("\nTest 6: Is age > 20? I predict True.")
print(age > 20)
print("\nTest 7: Is age < 30? I predict True.")
print(age < 30)
print("\nTest 8: Is age >= 25? I predict True.")
print(age >= 25)
print("\nTest 9: Is age <= 30? I predict True.")
print(age <= 30)
print("\nTest 10: Is name == 'John' and age == 25? I predict True.")
print(name == 'John' and age == 25)
print("\nTest 11: Is name == 'John' or age == 30? I predict True.")
print(name == 'John' or age == 30)
print("\nTest 12: Is 3 in numbers? I predict True.")
print(3 in numbers)
print("\nTest 13: Is 6 not in numbers? I predict True.")
print(6 not in numbers)


# 5-3. Alien Colors #1
print("\n")
print("Number 5-3:")
alien_color = 'green'
if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")


# 5-4. Alien Colors #2
print("\n")
print("Number 5-4:")
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
else:
    print("Congratulations! You just earned 10 points.")


# 5-5. Alien Colors #3
print("\n")
print("Number 5-5:")
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for the green alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for the red alien.")


# 5-6. Stages of Life
print("\n")
print("Number 5-6:")
age = 25

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


# 5-7. Favorite Fruit
print("\n")
print("Number 5-7:")
favorite_fruits = ['apple', 'banana', 'orange']

if 'apple' in favorite_fruits:
    print("You really like Apples!")
if 'banana' in favorite_fruits:
    print("You really like Bananas!")
if 'orange' in favorite_fruits:
    print("You really like Oranges!")
if 'grape' in favorite_fruits:
    print("You really like Grapes!")
if 'kiwi' in favorite_fruits:
    print("You really like Kiwis!")


# 5-8. Hello Admin
print("\n")
print("Number 5-8:")
usernames = ['Angelo', 'Mattia', 'Gabriel', 'Admin', 'Sani', 'Samuele']

for username in usernames:
    if username == 'Admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")


# 5-9. No Users
print("\n")
print("Number 5-9:")



# 5-10. Checking Usernames
print("\n")
print("Number 5-10:")



# 5-11. Ordinal Numbers
print("\n")
print("Number 5-11:")


