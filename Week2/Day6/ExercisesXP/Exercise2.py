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

bigger_dog = None
smaller_dog = None
if davids_dog.height > sarahs_dog.height:
    bigger_dog = davids_dog
    smaller_dog = sarahs_dog
else:
    bigger_dog = sarahs_dog
    smaller_dog = davids_dog

print(f"{bigger_dog.name} is bigger than {smaller_dog.name} by {bigger_dog.height - smaller_dog.height}cm.")
