import csv
import os
import random

class Character:
    def __init__(self, strName, strTitle, intStrength, intRizz, intDexterity, intCopper=0, intSilver=0, intGold=0):
        self.strName = strName
        self.strTitle = strTitle
        self.intStrength = intStrength
        self.intRizz = intRizz
        self.intDexterity = intDexterity
        self.intCopper = intCopper
        self.intSilver = intSilver
        self.intGold = intGold

    def __str__(self):
        return ("---------------\n"
                f"{self.strName} the {self.strTitle}\n"
                f"Strength: {self.intStrength}\n"
                f"Charisma: {self.intRizz}\n"
                f"Dexterity: {self.intDexterity}\n"
                "---------------")

    def displayMoney(self):
        print("You currently have:")
        print(f"Copper: {self.intCopper}")
        print(f"Silver: {self.intSilver}")
        print(f"Gold: {self.intGold}")

    def addMoney(self, intCopper, intSilver, intGold):
        self.intCopper += intCopper
        self.intSilver += intSilver
        self.intGold += intGold

    def loadFromFile(self, strName, strTitle, intStrength, intRizz, intDexterity, intCopper, intSilver, intGold):
        self.strName = strName
        self.strTitle = StrTtitle
        self.intStrength = intStrength
        self.intRizz = intRizz
        self.intDexterity = intDexterity
        self.intCopper = intCopper
        self.intSilver = intSilver
        self.intGold = intGold

def clear():
    """
    Clears the terminal on Linux, Mac and Windows
    """
    os.system("cls" if os.name == "nt" else "clear")

def createCharacter():
    """Gets input from the user and creates a character using that input

    Returns:
        Character: The players character
    """
    strName = input("What is your characters name? ")
    strTitle = input("What is your characters title? ")
    while True:
        try:
            intStrength = int(input("What is your characters strength stat? "))
            intRizz = int(input("What is your charisma stat? "))
            intDexterity = int(input("What is your dexterity stat? "))
            break
        except ValueError:
            clear()
            print("Stats must be number!")

    clear()
    return Character(strName, strTitle, intStrength, intRizz, intDexterity)

def saveCharacter(character):
    """Saves all character data to a csv file

    Args:
        character (Character): The players character
    """
    strSaveFile = input("Where do you want to save the character data? ")
    if os.path.exists(strSaveFile):
        strChoice = input(f"Are you sure you want to overwrite {strSaveFile}: [y/n] ").lower()
        if strChoice == "n":
            return

    with open(strSaveFile, "w") as file:
        fieldnames = ["Name", "Title", "Strength", "Charisma", "Dexterity", "Copper", "Silver", "Gold"]
        writer = csv.DictWriter(file, fieldnames)

        writer.writeheader()
        writer.writerow({"Name": character.strName, "Title": character.strTitle, "Strength": character.intStrength, "Charisma": character.intRizz, "Dexterity": character.intDexterity, "Copper": character.intCopper, "Silver": character.intSilver, "Gold": character.intGold})

def loadCharacter():
    """Loads all character data from a csv file

    Returns:
        Character: The loaded character data
    """
    while True:
        try:
            strLoadFile = input("What file do you want to load data from? ")

            with open(strLoadFile, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    return Character(row["Name"], row["Title"], row["Strength"], row["Charisma"], row["Dexterity"], row["Copper"], row["Silver"], row["Gold"])
        except FileNotFoundError:
            clear()
            print("File not found")
def addMoney(character):
    """Adds money to the wanted supplied character

    Args:
        Character (character): The players character
    """

    clear()
    while True:
        try:
            intCopper = int(input("Copper: "))
            intSilver = int(input("Silver: "))
            intGold = int(input("Gold: "))

            character.addMoney(intCopper, intSilver, intGold)
            break
        except ValueError:
            clear()
            print("Currency must be a number!")

def rollDice():
    """
    Gets the user to input a number and roll a dice with that amount of sides
    """
    clear()
    while True:
        try:
            # Gets the Amount of dice
            listDiceSides = []
            listRolledNums = []
            intDiceAmount = int(input("How many dice do you want to roll? "))

            # Gets the amount of sides on each dice
            for _ in range(0, intDiceAmount):
                listDiceSides.append(int(input("How many sides should the dice have? ")))

            # Generates a random number for each dice
            for i in range(0, intDiceAmount):
                listRolledNums.append(random.randint(1, listDiceSides[i]))

            # Prints the rolled numbers
            clear()
            print("You rolled:")
            for i in range(0, intDiceAmount):
                print(f"Die {i + 1}: {listRolledNums[i]}")

            break
        except ValueError:
            clear()
            print("Please input a number!")
