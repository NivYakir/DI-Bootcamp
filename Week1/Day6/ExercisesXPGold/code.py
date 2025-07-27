# Exercise 1: Birthday Lookup

birthday = {}
while len(birthday) != 5:
    name_input = input(f"Enter the person's name:\n")
    date_input = input(f"Enter the person's birthday using YYYY/MM/DD format:\n")
    birthday.update({name_input : date_input})
print("Welcome! You can look up the birthdays of the people in the list below!")
print(list(birthday.keys()))
while True:
    user_input = input("Enter a name to find out their birthday or type 'done' if you are finished:\n")
    if user_input.lower() == 'done':
        break
    if user_input.lower() not in birthday.keys():
        print(f"Sorry, we don't have the birthday information for {user_input}")
    else:
        print(f"{user_input}'s birthday is {birthday[user_input]}!")

# Exercise 2: Fruit Shop
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# 1
for fruit, price in items.items():
    if fruit[0] in ['a','e','i','o','u']:
        print(f"An {fruit} costs ${price}")
    else:
        print(f"A {fruit} costs ${price}")

# 2
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0

for fruit in items.keys():
    total_cost += (items[fruit]['price'] * items[fruit]['stock'])
print(total_cost)