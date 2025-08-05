# Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ''

    def is_18(self):
        '''Returns True if the Person is 18 years or older'''
        if self.age >= 18:
            return True
        else:
            return False
    
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        '''Adds a new member to the family'''
        member = Person(first_name, age)
        member.last_name = self.last_name
        self.members.append(member)

    def check_majority(self, first_name):
        '''Checks for a persons name in the family and determines whether or not they can go out depending on their age.'''
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):
        '''Prints the names and age of all the members of the family'''
        output = f"The {self.last_name} Family:\n\n"
        for member in self.members:
            output += f"{member.first_name}, {member.age} years old.\n"
        
        return output


family1 = Family('Yakir')
family1.born('Niv', 20)
family1.born('Cami', 12)
family1.born('Dan', 30)
family1.born('Ahsa', 19)
family1.check_majority('Cami')
print(family1.family_presentation())