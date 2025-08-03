# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat('Garfield', 12)
cat2 = Cat('Puss', 15)
cat3 = Cat('Sylvester', 17)

# Step 2: Create a function to find the oldest cat
def get_oldest(cat1,cat2,cat3):
    oldest_cat = None
    if cat1.age > cat2.age and cat1.age > cat3.age:
        oldest_cat = cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        oldest_cat = cat2
    else:
        oldest_cat = cat3

    print(f"The oldest cat is {oldest_cat.name}, and (s)he is {oldest_cat.age} years old.")

# Step 3: Print

get_oldest(cat1,cat2,cat3)