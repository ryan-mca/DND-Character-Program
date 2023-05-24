import configparser
import os
import random

class Character:
    def __init__(self, strName, strTitle, intStrength, intRizz, intDexterity):
        self.strName = strName
        self.strTitle = strTitle
        self.intStrength = intStrength
        self.intRizz = intRizz
        self.intDexterity = intDexterity
        self.intCopper = 0
        self.intSilver = 0
        self.intGold = 0

    def __str__(self):
        print(f"{self.strName} the {self.strTitle}")
        print(f"Strength: {self.intStrength}")
        print(f"Charisma: {self.intRizz}")
        print(f"Dexterity: {self.intDexterity}")

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

def rollDice():