# Angelo Mihalache
# 18/04/2024

print("Hello world!")
import random

#Personal Message
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today")

#Name Cases
upperCases = name.upper()
lowerCases = name.lower()
print(upperCases)
print(lowerCases)

#Famouse Quote 1 - 2
"Martin Luther King once said: I have a dream"
message = "I have a dream"
famousPerson = "Martin Luher King"
print (message + " once said "  + famousPerson)

#File Extension
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
print("\nGood news! We found a bigger dinner table.")


# 3-7. Shrinking Guest List:


# 3-8. Seeing the World:


# 3-9. Dinner Guests:


# 3-10. Every Function:


# 6-1. Person:


# 6-2. Favorite Numbers:


# 6-3. Glossary:


# 6-7. People:


# 6-8. Pets:


# 6-9. Favorite Places:


# 6-10. Favorite Numbers:


# 6-11. Cities:


# 6-12. Extensions:

