class User:
    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with {self.power} power!")
    
class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"attacking with arrows. {self.arrows} left")

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 30)

def player_attack(character):
    character.attack()

# player_attack(archer1)

for character in [wizard1, archer1]:
    player_attack(character)