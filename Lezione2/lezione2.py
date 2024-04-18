# Angelo Mihalache
# 18/04/2024

print("Hello world!")

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

#Names
names = ["Gianni", "Mario", "Flavio", "Andrea", "Matteo"]
friend1 = names[0]
friend2 = names[1]
friend3 = names[2]
friend4 = names[3]
friend5 = names[4]
listFriends = [friend1, friend2, friend3, friend4, friend5] #questa lista è stata creata solo a scopo per un check
print (listFriends)

#Greetings
for name in names:
    print ("Grazie mille per aver partecipato all'attività", name )

#Your own list
vehicles = ["an S2000", "an s13", "an honda civic", "a mitsubishi evo", "a mitsubishi lancer", "an harley davinson"]
for vehicle in vehicles:
    print("Surely", vehicle + "is in my dream garage")
