# Exercise 1: Birthday Lookup

birthdays = {}

while len(birthdays) != 5:
    name_input = input(f"Please enter a name:\n")
    date_input = input(f"Please enter their birthday using YYYY/MM/DD format:\n")
    birthdays.update({name_input : date_input})

print("Welcome! You can look up the birthdays of the people in the list!")
print(list(birthdays.keys()))
while True:
    person = input(f"Enter a name to find out their birthday or type 'quit' if you are finished.\n")
    birthdate = birthdays[name_input]
    if person == 'quit':
        break
    elif person in birthdays.keys():
        print(f"{person} was born on {birthdate}")
    else:
        print(f"This person is not on the list!")

# Exercise 4: Fruit Shop
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for fruit,price in items.items():
    print(f"A {fruit} costs ${price}")

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0
for fruit in items.keys():
    cost = items[fruit]['price'] * items[fruit]['stock']
    total_cost += cost

print(f"The total cost is ${total_cost}")