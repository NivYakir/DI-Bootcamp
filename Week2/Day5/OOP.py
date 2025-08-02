# OOP - Object Oriented Programming

# Classes and Object

# How to create a class:

class Dog:
    
    # The constructor:
    def __init__(self, name, color, age, is_trained=False):
        # print("The obj is being created")
        self.name = name                # self.name = KEY, after the = is the VALUE
        self.color = color
        self.age = age
        self.is_trained = is_trained

# Accessing values using .method // notice that you use .key to get the value
dog1 = Dog('Rex', 'brown', 10)
dog2 = Dog('Mushu', 'brown', 5)
dog3 = Dog('Max', 'white', 7, is_trained=True)

print(dog1.name) # Rex
print(dog1.color) # brown
print(dog1.age) # 10
dog1.breed = 'Poodle'
print(dog1.__dict__) # 'internal' dictionary that python created for object # {'name' : 'Rex', 'color' : 'brown', 'age' : 10}
print(dog1.breed)

dog2 = Dog('Mushu', 'brown', 5) # running this line, will call the print inside the constructor

# Create a new attribute to the dog class called is_trained() the value is a boolean and the default is False. 
# Then run the code. What happened with the objects that were created before this new attribute was added


print(dog3.__dict__)
print(type(dog3)) # class __main__.Dog
print(dog3.age) # 7

# Behaviors = Methods

# functions > methods
# methods = functions related to a certain class

class Dog:
    def __init__(self, name, color, age, is_trained=False):
        self.name = name               
        self.color = color
        self.age = age
        self.is_trained = is_trained

    def bark(self):
        print(f"{self.name} is barking!")
    
    def is_hungry(self):
        self.bark()
        print(f"{self.name} is hungry!")
    
    def run(self):
        if self.age <= 5:
            print(f"{self.name} is running really fast!")
        elif self.age > 5 and self.age <= 9:
            print(f"{self.name} is running!")
        else:
            print(f"{self.name} doesn't want to run.")

    def walk(self, meters):
        print(f"{self.name} is walking {meters} meters.")

    def rename(self, new_name):
        self.name = new_name
        return self


dog1 = Dog('Rex', 'brown', 10)
dog2 = Dog('Mushu', 'brown', 5)
dog3 = Dog('Max', 'white', 7, is_trained=True)

my_dog = Dog('Max', 'black', 10)
my_dog.is_hungry()
my_dog.run()

# Create a method called walk that takes parameter (meters : int) and prints "dog's  name is walking {meter} meters."

my_dog.walk(200)

dog2.walk(100)      # 'Mushu is walking 1000 meters'

Dog.walk(dog2,1000) # 'Mushu is walking 1000 meters'

# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below


# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()
# # IS THE SAME AS:
# dell_computer.description("Mark")
