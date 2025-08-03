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
