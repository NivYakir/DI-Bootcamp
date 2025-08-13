# Dungeons and Dragons
import random

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def roll(self):
        rolls = []
        for _ in range(4):
            rolls.append(random.randint(1,6))
        rolls = sorted(rolls)
        return sum(rolls[1:])

    @property
    def strength(self):
        return self.roll()
    
    @property
    def dexterity(self):
        return self.roll()
    
    @property
    def constitution(self):
        return self.roll()
    
    @property
    def intelligence(self):
        return self.roll()
    
    @property
    def wisdom(self):
        return self.roll()
    
    @property
    def charisma(self):
        return self.roll()
    
    def __str__(self):
        return f"""Name: {self.name}
Age: {self.age}
Strength: {self.strength}
Dexterity: {self.dexterity}
Constitution: {self.constitution}
Intelligence: {self.intelligence}
Wisdom: {self.wisdom}
Charisma: {self.charisma}"""
    


class Game:
    def __init__(self):
        total_players = int(input("How many players are there? "))
        self.total_players = total_players

    def create_characters(self):
        char_list = []
        for _ in range(self.total_players):
            name_input = input("Enter your character's name: ")
            age_input = input("How old is your character? ")
            c =  Character(name_input, age_input)
            char_list.append(c)

        return char_list
    

g1 = Game()

