import random

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

# Exercise 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        print(f"{self.name} is barking...")

    def run_speed(self):
        return (round((self.weight / self.age) * 10, 2))
    
    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
            return f"{self.name} won the fight."
        else:
            return f"{other_dog.name} won the fight."
        

dog1 = Dog('Floof', 11, 35)
dog2 = Dog('Bigfoot', 6, 60)
dog3 = Dog('Chewie', 4, 15)

# Step 3:

dog1.bark()
dog2.bark()
dog3.bark()

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog3.fight(dog1))
print(dog2.fight(dog3))

# Exercise 3

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking..."

    def run_speed(self):
        return (round((self.weight / self.age) * 10, 2))
    
    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
            return f"{self.name} won the fight."
        else:
            return f"{other_dog.name} won the fight."
        
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    
    def train(self):
        print(self.bark())
        self.trained = True
        return self
    
    def play(self, *args):
        output = ''
        for i in range(len(args) - 1):
            output += args[i].name + ', '
        output += 'and ' + args[-1].name

        return output + ' all play together.'

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]

        if self.trained == True:
            return f"{self.name} {random.choice(tricks)}"
        else:
            return self.bark()

dog1 = Dog('Floof', 11, 35)
dog2 = Dog('Bigfoot', 6, 60)
dog3 = Dog('Chewie', 4, 15)
dog4 = Dog('Mushu', 5, 20)
dog5 = Dog('Bruce', 6, 50)
petdog1 = PetDog('Lucky', 4, 45)
petdog2 = PetDog('Lyca', 3, 33)
petdog1.train()

print(petdog1.play(dog1, dog2, dog3, dog4, dog5))
print(petdog1.do_a_trick())
print(petdog2.do_a_trick())

# Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ''

    def is_18(self):
        '''Returns True if the Person is 18 years or older'''
        if self.age >= 18:
            return True
        else:
            return False
    
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        '''Adds a new member to the family'''
        member = Person(first_name, age)
        member.last_name = self.last_name
        self.members.append(member)

    def check_majority(self, first_name):
        '''Checks for a persons name in the family and determines whether or not they can go out depending on their age.'''
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):
        '''Prints the names and age of all the members of the family'''
        output = f"The {self.last_name} Family:\n\n"
        for member in self.members:
            output += f"{member.first_name}, {member.age} years old.\n"
        
        return output


family1 = Family('Yakir')
family1.born('Niv', 20)
family1.born('Cami', 12)
family1.born('Dan', 30)
family1.born('Ahsa', 19)
family1.check_majority('Cami')
print(family1.family_presentation())