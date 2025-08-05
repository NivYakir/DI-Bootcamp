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