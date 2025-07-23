# Exerice 1: Favorite Numbers

my_fav_numbers = {7,13,21,42,49,69}
my_fav_numbers.add(100)
my_fav_numbers.add(220)
print(my_fav_numbers)

my_fav_numbers.remove(220)
print(my_fav_numbers)

friend_fav_numbers = {18,29,32,50,77}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2

my_tuple = (1,2,3,4)
# my_tuple.append(5)

print(my_tuple) # Error: cannot add elements to a tuple

# Exercise 3: List Manipulation
basket = ['Banana','Apples','Oranges','Blueberries']

basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0,'Apples')
print(basket.count('Apples')) # 2
basket.clear()
print(basket)

# Exercise 4: Floats
# A float is a number class type that includes a decimal whereas an integer is a whole number.

my_list = []

for i in range(2,6):
    my_list.append(i - 0.5)
    my_list.append(i)
print(my_list)

# Exercise 5: For Loop

for i in range(1, 21):
    print(i)

for index, num in enumerate(range(1,20)):
    if index % 2 == 0:
        print(num)

# Exercise 6: While Loop

my_name = 'Niv'
while True:
    user_name = input("Please write your name: ")
    if user_name.upper() == my_name.upper():
        break
    else:
        continue

# Exercise 7: Favorite Fruits

user_input = input("Enter your favorite fruits, separate by spaces: ")
fruits = user_input.split()

fav_fruit = input("Please input the of any fruit: ")
if fav_fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings

toppings = []
cost = 10.0
while True:
    topping = input("Please enter your favorite topping: ")
    if topping.upper() == 'QUIT':
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza")
        cost += 2.5
print(f"Your Toppings: {toppings}\n" f"Total Cost: ${cost}")

# Exercise 9: Cinemax Tickets

total_cost = 0
while True:
    user_age = int(input("Please input your age: "))
    if user_age == 0:
       break
    elif user_age < 3:
        total_cost += 0
    elif user_age >= 3 and user_age <= 12:
        total_cost += 10
    else:
        total_cost += 15
print(f"Your total cost is ${total_cost}")

# Bonus:

age_input = input("Please enter the age of each person, separated by a space: ")
teens_list = age_input.split()
teens_list = [int(age) for age in teens_list]
teens_list = [age for age in teens_list if 16 <= age <= 21]
print(teens_list)

# Exercise 10: Sandwich Orders

sandwich_orders = ['Tuna', 'Pastrami', 'Avocado', 'Pastrami', 'Egg', 'Chicken', 'Pastrami']
updated_orders = [order for order in sandwich_orders if order != 'Pastrami']

finished_orders = []
for order in updated_orders:
    print(f"I made your {order} Sandwich")
    finished_orders.append(order)
print(f"Here is a list of your finished sandwiches: {finished_orders}")