# Angelo Mihalache
# 18/04/2024
import random


print("Hello world!")


# 2-3. Personal Message
print("\n")
print("Number 2-3:")
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today")


# 2-4. Name Cases
print("\n")
print("Number 2-4:")
upperCases = name.upper()
lowerCases = name.lower()
print(upperCases)
print(lowerCases)


# 2-5 / 2-6. Famous Quote
print("\n")
print("Number 2-5 / 2-6:")
"Martin Luther King once said: I have a dream"
message = "I have a dream"
famousPerson = "Martin Luher King"
print (message + " once said "  + famousPerson)


# 2-8. File Extensions
print("\n")
print("Number 2-8:")
fileName = "python_notes.txt"
fileNameCorrect = fileName.removesuffix(".txt")
print(fileNameCorrect)


# 3-1. Names
print("\n")
print("Number 3-1.")
names = ["Gianni", "Mario", "Flavio", "Andrea", "Matteo"]
friend1 = names[0]
friend2 = names[1]
friend3 = names[2]
friend4 = names[3]
friend5 = names[4]
listFriends = [friend1, friend2, friend3, friend4, friend5] #questa lista è stata creata solo a scopo per un check
print (listFriends)


# 3-2. Greetings
print("\n")
print("Number 3-2.")
for name in names:
    print ("Grazie mille per aver partecipato all'attività", name )


# 3-3. Your own list
print("\n")
print("Number 3-3.")
vehicles = ["an S2000", "an s13", "an honda civic", "a mitsubishi evo", "a mitsubishi lancer", "an harley davinson"]
for vehicle in vehicles:
    print("Surely", vehicle + " is in my dream garage")


# 3-4. Guest List
print("\n")
print("Number 3-4.")
guests = ["Travis Scott", "Ye", "mamma", "Mattia Rò", "Cerratti", "Cuozzo"]
for guest in guests:
    print("Hey", guest + ", want to join us or dinner?")


# 3-5. Changing Guest List
print("\n")
print("Number 3-5.")
for guest in guests:
    print("Hey", guest + ", want to join us or dinner?")
CMIguest = random.choice(guests)
print("\nTonight", CMIguest, " can't make to the dinner sadly :(")
guests.remove(CMIguest)
new_guest = "papà"
guests.append(new_guest)
print("\nHey", new_guest + ", want to join us or dinner?")


# 3-6. More Guests
print("\n")
print("Number 3-6.")
for guest in guests:
    print("Hey", guest + ", want to join us or dinner?")
new_guest_beginning = "nonna"
guests.insert(0, new_guest_beginning)
new_guest_middle = "nonno"
middle_index = len(guests) // 2
guests.insert(middle_index, new_guest_middle)
new_guest_end = "sorella"
guests.append(new_guest_end)
print("\nUpdated guest list:")
for guest in guests:
    print("Hey", guest + ", want to join us for dinner?")
print("\nGood news! We found a bigger dinner table")


# 3-7. Shrinking Guest List:
print("\n")
print("Number 3-7.")
print("\nSorry, the new dinner table won't arrive in time. We can only invite two people")
while len(guests) > 2:
    removed_guest = guests.pop()
    print("Sorry", removed_guest + ", we can't invite you to dinner")
print("\nInvited guests:")
for guest in guests:
    print("Hey", guest + ", you're still invited to dinner XD")
del guests[-2:]
print("\nGuest list after dinner:", guests)


# 3-8. Seeing the World:
print("\n")
print("Number 3-8.")
places = ["Tokyo", "Paris", "Hawaii", "New York", "Amsterdam"]
print(places)
print("\nSorted alphabetically: ")
print(sorted(places))
print("Original order preserved: ")
print(places)
print("\nSorted in reverse-alphabetical order: ")
print(sorted(places, reverse=True))
print("Original order preserved: ")
print(places)
print("\nReversed order using reverse(): ")
places.reverse()
print(places)
print("\nReversed again to original order: ")
places.reverse()
print(places)
print("\nSorted alphabetically using sort(): ")
places.sort()
print(places)
print("\nSorted in reverse-alphabetical order using sort(): ")
places.sort(reverse=True)
print(places)


# 3-9. Dinner Guests:
print("\n")
print("Number 3-9.")
num_invited = len(guests)
print("Number of people invited to dinner:", num_invited)


# 3-10. Every Function:
print("\n")
print("Number 3-10.")
fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple"]
print("Original list of fruits:")
print(fruits)

# 1
random_fruit = random.choice(fruits)
print("\nRandom fruit (", random_fruit, ") is out of the list. ")
fruits.remove(random_fruit)
new_fruit = "Grapes"
fruits.append(new_fruit)
print("New fruit (", new_fruit, ") is on of the list. ")
print("Updated fruit list:")
print(fruits)

# 2
new_fruit_beginning = "Lemon"
fruits.insert(0, new_fruit_beginning)
new_fruit_middle = "Kiwi"
middle_index = len(fruits) // 2
fruits.insert(middle_index, new_fruit_middle)
new_fruit_end = "Peach"
fruits.append(new_fruit_end)
print("\nNew fruits on top/bottom and center of the list:")
print(fruits)

# 3
num_fruits = len(fruits)
print("\nNumber of the fruit list:", num_fruits)
while len(fruits) > 5:
    fruits.pop()
num_fruits = len(fruits)
print("Number of the new fruit list:", num_fruits)

# 4
print("\nLast original fruit list:")
print(fruits)
print("\nSorted alphabetically: ")
print(sorted(fruits))
print("\nSorted in reverse-alphabetical order: ")
print(sorted(fruits, reverse=True))
print("\nReversed order using reverse(): ")
fruits.reverse()
print(fruits)
print("\nReversed again to original order: ")
fruits.reverse()
print(fruits)
print("\nSorted alphabetically using sort(): ")
fruits.sort()
print(fruits)
print("\nSorted in reverse-alphabetical order using sort(): ")
fruits.sort(reverse=True)
print(fruits)


# 6-1. Person:
print("\n")
print("Number 6-1.")
person = {
    "first_name": "Angelo",
    "last_name": "Mihalache",
    "age": 19,
    "city": "Rome"
}

print("First Name:", person["first_name"])
print("Last Name:", person["last_name"])
print("Age:", person["age"])
print("City:", person["city"])


# 6-2. Favorite Numbers:
print("\n")
print("Number 6-2.")
favorite_numbers = {
    "Angelo": 7,
    "Gabriel": 12,
    "Samuele": 5,
    "Davide": 8,
    "Mattia": 3
}

for person, number in favorite_numbers.items():
    print(f"{person}'s favorite number is {number}.")


# 6-3. Glossary:
print("\n")
print("Number 6-3.")
glossary = {
    "variable": "A named storage location in a program that holds data, which can be modified during program execution.",
    "function": "A named block of code that performs a specific task. Functions can take inputs (parameters) and optionally return an output.",
    "loop": "A control flow statement that allows code to be executed repeatedly based on a condition.",
    "dictionary": "A collection of key-value pairs where each key is associated with a value. Dictionaries are unordered, mutable, and indexed.",
    "list": "An ordered collection of items that can contain elements of different data types. Lists are mutable, meaning their elements can be changed after they are created."
}

for word, meaning in glossary.items():
    print(f"{word.capitalize()}:")
    print(meaning)
    print()


# 6-7. People:
print("\n")
print("Number 6-7.")
person1 = {
    "first_name": "Angelo",
    "last_name": "Mihalache",
    "age": 19,
    "city": "Rome"
}

person2 = {
    "first_name": "Mattia",
    "last_name": "Rò",
    "age": 18,
    "city": "Amsterdam"
}

person3 = {
    "first_name": "Andrea",
    "last_name": "Capasso",
    "age": 20,
    "city": "Napoli"
}

people = [person1, person2, person3]

for person in people:
    print("First Name:", person["first_name"])
    print("Last Name:", person["last_name"])
    print("Age:", person["age"])
    print("City:", person["city"])
    print()


# 6-8. Pets:
print("\n")
print("Number 6-8.")



# 6-9. Favorite Places:
print("\n")
print("Number 6-9.")



# 6-10. Favorite Numbers:
print("\n")
print("Number 6-10.")



# 6-11. Cities:
print("\n")
print("Number 6-11.")



# 6-12. Extensions:
print("\n")
print("Number 6-12.")

