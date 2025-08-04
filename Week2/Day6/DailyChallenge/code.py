# Old MacDonald's Farm

class Farm:
    '''This class represents a Farm and its animals'''
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        '''Add an animal to the farm based on animal type and count'''
        if animal_type in self.animals.keys():
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

        return self

    def get_info(self):
        '''return a string that displays the farm's name, the animals and their counts, and the “E-I-E-I-0!” phrase'''
        output = f"{self.name}'s Farm\n\n"
        for k, v in self.animals.items():
            output += f"{k} : {v}\n"

        output += '\n     E-I-E-I-O'

        return output
    
    def get_animal_types(self):
        '''Returns a sorted list of all the animals in the Farm'''
        my_list = sorted(self.animals)
        return my_list
    
    def get_short_info(self):
        '''Returns a string with information about what animals can be found on the farm'''
        animal_list = []
        # Check the count of the animal to know if we should add an s to the end of the animal type
        for animal, count in sorted(self.animals.items()):
            if count == 1:
                animal_list.append(animal)
            else:
                animal_list.append(animal + 's')

        animals_str = ''
        if len(animal_list) == 1:
            animals_str = animal_list[0]
        elif len(animal_list) == 2:
            animals_str = f"{animal_list[0]} and {animal_list[1]}"
        else:
            animals_str = ', '.join(animal_list[:-1]) + ' and ' + animal_list[-1]
        
        return f"{self.name}'s farm has {animals_str}."
    

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())