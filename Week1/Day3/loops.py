# For Loops 

# Basic iteration

fruits = ['apple', 'banana', 'kiwi', 'mango']

for fruit in fruits:
    print(fruit)

# sequences that we can loop through:
# strings
for char in 'Garry':
    print(char)

# list: above example

# tuples and sets
languages = ('PT', 'ES', 'IT')
for lang in languages:
    print(lang)

# range()

for i in range(0, 11, 2):
    print('hello', i)

# enumerate

for i, fruit in enumerate(fruits):
    if fruit == 'apple':
        fruits[i] = 'Windows is better'
    else:
        print(f"Fruit {i} is {fruit}") # Fruit 0 is 'apple'
                                       # Fruit 1 is 'banana'
print(fruits)
