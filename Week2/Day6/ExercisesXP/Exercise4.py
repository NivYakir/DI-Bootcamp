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
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print('That animal is not in the Zoo.')
        return self

    def sort_animals(self):
        '''Returns a dictionary where the animals are groups based on their first letter'''
        result = {}
        self.animals.sort()
        for animal in self.animals:
            if animal[0] not in result.keys():
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