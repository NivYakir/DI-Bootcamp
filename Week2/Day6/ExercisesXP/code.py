# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Max", 8)
cat2 = Cat("Darcy", 10)
cat3 = Cat("Puss", 6)

def find_oldest_cat(self, cat1, cat2):
    oldest = ''
    if self.age > cat1.age and self.age > cat2.age:
        oldest = self
    elif cat1.age > self.age and cat1.age > cat2.age:
        oldest = cat1
    else:
        oldest = cat2
    print(f"The oldest cat is {oldest.name}, and {oldest.age} years old.")

find_oldest_cat(cat1,cat2,cat3)

# Exercise 2: 