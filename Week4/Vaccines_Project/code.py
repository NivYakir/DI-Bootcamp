from collections import deque

class Human:
    """Represents a citizen of a city"""
    def __init__(self, id_number: str, name: str, age: int, prio: bool, blood_type: str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.prio = prio
        self.blood_type = blood_type
        self.family = []
    
    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)
        return self
    
    def __str__(self):
        return f"{self.name}-{self.age}"
    




class Queue:
    """Represents a queue of humans waiting to receive a vaccine"""
    def __init__(self):
        self.humans = deque()

    def add_person(self, person):
        if person.age > 60 or person.prio:
            self.humans.appendleft(person)
        else:
            self.humans.append(person)
    
    def find_in_queue(self, person: Human):
        return self.humans.index(person)
    
    def swap(self, person1, person2):
        i, j = self.humans.index(person1), self.humans.index(person2)
        self.humans[i], self.humans[j] = self.humans[j], self.humans[i]

        return self
    
    def get_next(self):
        return self.humans[0]
    
    def get_next_blootype(self, blood_type):
        for p in self.humans:
            if p.blood_type == blood_type:
                return p
        else:
            return f"There are currently no Humans with blood type {blood_type} in the queue."
        
    def sort_by_age(self):
        self.humans = deque(sorted(
            self.humans,
            key=lambda p: (0 if p.prio else 1, -p.age)   # checks if the user is prio, then checks based on who is older (descending order)
        ))
        return self

    def __str__(self):
        return '\n'.join(str(p) for p in self.humans)
    





h1 = Human('1', 'Niv', 30, False, 'AB')
h2 = Human('2', 'Cami', 22, True, 'O')
h3 = Human('3', 'Dan', 29, False, 'O')
h4 = Human('4', 'Rony', 67, False, 'A')
h5 = Human('5', 'Ahsa', 61, True, 'O')
h6 = Human('6', 'Dor', 2, False, 'O')

h1.add_family_member(h6)

q1 = Queue()

# q1.add_person(h1)
# q1.add_person(h2)
# q1.add_person(h3)
# q1.add_person(h4)
# q1.add_person(h5)
# print(q1.sort_by_age())