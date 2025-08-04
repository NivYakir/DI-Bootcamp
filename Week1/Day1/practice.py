# Exercise 4: Zoo

class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animial):
        '''Adds a new animal to the animals list'''
        if new_animial not in self.animals:
            self.animals.append(new_animial)
        else:
            print('This animal is already in the Zoo.')

        return self

    def get_animals(self):
        '''Prints all the animals that are currently in animals list.'''
        print(self.animals)

    def sell_animal(self, animal_sold):
        '''Removes an animal if it is in animals list'''
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"There is no {animal_sold} in the Zoo for sale.")
    
    def sort_animals(self):
        '''Returns a dictionary of the animals, sorted alphabetically by groups'''
        result = {}
        self.animals.sort()
        for item in self.animals:
            if item[0] not in result.keys():
                result[item[0]] = [item]
            else:
                result[item[0]].append(item)
        return result
    
    def get_groups(self):
        result = self.sort_animals()

        for k,v in result.items():
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
zoo1.get_groups()




