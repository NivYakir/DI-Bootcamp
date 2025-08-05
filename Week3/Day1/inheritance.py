# class Parent:
#     def speak(self): 
#         print(f'Parent speaking...')

# class Child(Parent):
#     def speak(self):
#         print(f"Child speaking...")

# class GrandChild(Child):
#     pass


# obj1 = Child()
# obj1.speak()       # Child speaking... (will always inherit from the closes class, starting with itself)

# obj2 = GrandChild()
# obj2.speak()

class Animal:
    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs
    
    def sleep(self):
        return f"{self.name} is sleeping - from Animal"


class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained
        self.age = age
    
    def bark(self):
        return f"{self.name} is barking."


class Cat(Animal):
    def __init__(self, name, family, legs, friendly, age, nickname):
        super().__init__(name, family, legs)
        self.friendly = friendly
        self.age = age
        self.nickname = nickname
    
    def meow(self):
        return f"{self.name} is meowing."
    
    def get_crazy(self):
        if self.friendly:
            return f"{self.name} doesn't get crazy"
        else:
            return f"{self.name} is running in full power"


class Alien:
    def __init__(self, name, planet):
        self.personal_name = name
        self.planet = planet

    def bark(self):
        return f"{self.name} goes Ululululululu"


class AlienDog(Alien, Dog):
    def __init__(self, name, family, legs, trained, age, planet):
        Alien.__init__(self, name, planet)
        Dog.__init__(self, name, family, legs, trained, age)


class AlienCat(Cat, Alien):
    def __init__(self, name, family, legs, friendly, age, nickname, planet):
        Cat.__init__(self, name, family, legs, friendly, age, nickname)
        Alien.__init__(self, name, planet)
    
    def fly_away(self):
        return self.get_crazy() + ' as an Alien Cat'




dog1 = Dog('Rex','Canine', 4, True, 5)
# print(dog1.bark())
# print(dog1.sleep())


alien_dog1 = AlienDog('Buba', 'Canine', 6, True, 135, 'Jupiter')
# print(alien_dog1.bark())

alien_cat1 = AlienCat('Moxy', 'Feline', 6, False, 61, 'Rico',' Mars')
print(alien_cat1.fly_away())