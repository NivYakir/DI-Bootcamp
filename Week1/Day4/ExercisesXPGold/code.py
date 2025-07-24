# Exercise 1: Concatenate Lists

list_a = [1,2,3,4]
list_b = [5,6,7,8]
list_a.extend(list_b)
print(list_a)

# Exercise 2: Range of Numbers

for num in range(1500, 2500):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

# Exercise 3: Check the Index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name_input = input("Please enter your name: ")
for index, name in enumerate(names):
    if name_input.upper() == name.upper():
        print(index)
        break

# Exercise 4: Greatest Number

