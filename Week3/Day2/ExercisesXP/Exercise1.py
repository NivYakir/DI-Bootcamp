# Exercise 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


bengal1 = Bengal('Bibi', 8)
chart1 = Chartreux('Charles', 5)
siam1 = Siamese('Sam', 4)

all_cats = [bengal1, chart1, siam1]
sara_pets = Pets(all_cats)
sara_pets.walk()