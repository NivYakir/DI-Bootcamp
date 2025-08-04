# Exercise 4: Afternoon at the Zoo

class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    
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


zoo1 = Zoo("San Diego Zoo")
zoo1.add_animal('Elephant')
zoo1.add_animal('Anaconda')
zoo1.add_animal('Alligator')
zoo1.add_animal('Gorilla')
zoo1.add_animal('Bear')
zoo1.add_animal('Chameleon')
zoo1.add_animal('Leopard')
zoo1.add_animal('Chimpanzee')
zoo1.add_animal('Baboon')
zoo1.add_animal('Eel')
zoo1.add_animal('Zebra')
zoo1.add_animal('Lion')
zoo1.sell_animal('Dragon')
zoo1.sell_animal('Bear')
zoo1.get_groups()
