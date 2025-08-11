from datetime import datetime, date

# OOP and Modules

# Class Attributes

class Person:

    id_number = 1 

    def __init__(self, name, last_name, birth_date):
        self.name = self.format_name(name)
        self.last_name = self.format_name(last_name)
        self.birth_date = self.parse_birthdate(birth_date)
        Person.id_number += 1

    @staticmethod
    def parse_birthdate(date_str):
        return datetime.strptime(date_str, '%d-%m-%Y').date()

    @staticmethod
    def format_name(name):
        if not name[0].isupper():
            return name.capitalize()
        else:
            return name
    
    @classmethod
    def from_age(cls, name, last_name, age):
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = f"1-1-{birth_year}"
        return cls(name, last_name, birth_date)
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    
    def __str__(self):
        return f"name: {self.name}\nlast name: {self.last_name}\nage: {self.age}"
    
    def __repr__(self):
        return f'{self.__dict__}' # provides useful info to the developer
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __eq__(self, other):
        return self.age == other.age





p1 = Person('jon', 'snow', '21-08-1990')  # because of @staticmethod format_name, the first/last name will automatically be capitalized/formatted
print(p1)
# print(type(p1.birth_date))
# print(f"{p1.name} {p1.last_name}") # Jon Snow

p2 = Person.from_age('Arya','stark', 18)
p3 = Person.from_age('Ned', 'Stark', 49)

print(p1.age)
print(p1 > p2)
print(p2 == p3)
# print(p2.birth_date)

# print(p1.age)
# p2 = Person('Jon', 'Doe', '01-05-1990')

# print(Person.format_name('niv'))
