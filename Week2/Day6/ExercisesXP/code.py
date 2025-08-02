# Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects

cat1 = Cat('Garfield', 12)
cat2 = Cat('Puss', 7)
cat3 = Cat('Sylvester', 10)

def get_oldest(cat1,cat2,cat3):
    oldest_cat = None
    if cat1.age > cat2.age and cat1.age > cat3.age:
        oldest_cat = cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        oldest_cat = cat2
    else:
        oldest_cat = cat3

    print(f"The oldest cat is {oldest_cat.name}, and (s)he is {oldest_cat.age} years old.")

get_oldest(cat1,cat2,cat3)

# Exercise 2: Dogs
# Step 1 - Create Dog Class + Methods

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height * 2}cm high!")

# Step 2 - Create Dog objects

davids_dog = Dog('Max', 64)
sarahs_dog = Dog('Macy', 42)

# Step 3 - Print Dog Details and Call Methods

print(f"David's dog is named {davids_dog.name} and his height is {davids_dog.height}cm.")
print(f"Sarah's dog is named {sarahs_dog.name} and her height is {sarahs_dog.height}cm.")
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4 - Compare the Dog Sizes:

taller_dog = None
shorter_dog = None
if davids_dog.height > sarahs_dog.height:
    taller_dog = davids_dog
    shorter_dog = sarahs_dog
else:
    taller_dog = sarahs_dog
    shorter_dog = davids_dog

print(f"{taller_dog.name} is taller than {shorter_dog.name} by {taller_dog.height - shorter_dog.height}cm.")


# Exercise 3: Who's the Song Producer?

class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for word in self.lyrics:
            print(word)

stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise 4: Afternoon at the Zoo
class Zoo:
    def __init__(self,zoo_name,animals=[]):
        self.zoo_name = zoo_name
        self.animals = animals
    
    def add_animal(self, new_animal):
        '''Adds an animal into the Zoo if one doesn't already exist'''
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print("Animal is already in the zoo.")
        return self

    def get_animals(self):
        '''Prints all the animals in the Zoo.'''
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        '''Sell(remove) an animal if it is in the Zoo'''
        if animal_sold.upper() in self.animals.upper():
            self.animals.remove(animal_sold)
        else:
            print('That animal is not in the Zoo.')
        return self

    def sort_animals(self):
        '''Returns a dictionary where the animals are groups based on their first letter'''
        result = {}
        self.animals.sort()
        for animal in self.animals:
            if animal[0].upper() not in result.keys():
                result[animal[0]] = [animal]
            else:
                result[animal[0]].append(animal)
        return result

    def get_groups(self):
        '''Prints a list of groups of animals based on their first letter. Ordered alphabetically'''
        temp = self.sort_animals()
        for k, v in temp.items():
            print(f"{k} : {v}")


my_zoo = Zoo("Prague Zoo")
my_zoo.add_animal('Zebra')
my_zoo.add_animal('Gorilla')
my_zoo.add_animal('Eagle')
my_zoo.add_animal('Elephant')
my_zoo.get_animals()
my_zoo.add_animal('Giraffe')
my_zoo.add_animal('Hippo')
my_zoo.add_animal('Hyena')
my_zoo.add_animal('Beaver')
my_zoo.add_animal('Baboon')
my_zoo.sell_animal('Elephant')
my_zoo.get_animals()

my_zoo.get_groups()