import random

consonants = "aeioubcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
randomName = ""
validNumberOfParts = False

while not validNumberOfParts:
    try:
        partsOfName = input("How many parts of the name do you want? ")
        partsOfName = int(partsOfName)
        validNumberOfParts = True
    except:
        print("You didn't enter a valid number, yo.")

for part in range(partsOfName):
    currentPartValid = False
    while not currentPartValid:
        try:
            if part == 0:
                currentNameLength = input("How long do you want the first part of the name to be? ")
                currentNameLength = int(currentNameLength)
                currentPartValid = True
            else:
                currentNameLength = input("How long do you want the next part of the name to be? ")
                currentNameLength = int(currentNameLength)
                currentPartValid = True
        except:
            print("You didn't enter a valid number, yo.")
    vowelOrConsonant = random.randint(0,1)
    i = 0
    while i < int(currentNameLength):
        if vowelOrConsonant == 0:
            randomName += consonants[random.randint(0, 25)]
            vowelOrConsonant = 1
        elif vowelOrConsonant == 1:
            randomName += vowels[random.randint(0, 4)]
            vowelOrConsonant = 0
        i += 1
    randomName += " "

print(randomName[:-1])
