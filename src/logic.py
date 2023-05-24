import configparser
import os
import random

class Character:
    def __init__(self, name, title, strength, rizz, dexterity):
        self.name = name
        self.title = title
        self.strength = strength
        self.rizz = rizz
        self.dexterity = dexterity
        self.copper = 0
        self.silver = 0
        self.gold = 0

    def __str__(self):
        print(f"{self.name} the {self.title}")
        print(f"Strength: {self.strength}")
        print(f"Charisma: {self.rizz}")
        print(f"Dexterity: {self.dexterity}")

    def displayMoney(self):
        print("You currently have:")
        print(f"Copper: {self.copper}")
        print(f"Silver: {self.silver}")
        print(f"Gold: {self.gold}")

    def addMoney(self, copper, silver, gold):
        self.copper += copper
        self.silver += silver
        self.gold += gold

    def loadFromFile(self, name, title, strength, rizz, dexterity, copper, silver, gold):
        self.name = name
        self.title = title
        self.strength = strength
        self.rizz = rizz
        self.dexterity = dexterity
        self.copper = copper
        self.silver = silver
        self.gold = gold
