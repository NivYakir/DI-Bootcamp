import random

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