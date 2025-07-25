# Exercise 1: Converting Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))
print(my_dict)

# Exercise 2: Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0
for name, age in family.items():
    if age < 3:
        print(f"{name}'s ticket price is FREE")
    elif age >= 3 and age <= 12:
        print(f"{name}'s ticket price is $10")
        total_cost += 10
    else:
        print(f"{name}'s ticket price is $15")
        total_cost += 15
print(f"Total Price is ${total_cost}. Hope you enjoy!")

# BONUS

my_family = {}
total_cost = 0
while True:
    user_input = input("Enter family member (Name/Age) or type 'done' to finish:\n")
    if user_input == 'done':
        break
    else:
        name, age = user_input.split('/')
        age = int(age)
        my_family[name] = age

        if age < 3:
            print(f"{name}'s ticket price is FREE")
        elif age >= 3 and age <= 12:
            print(f"{name}'s ticket price is $10")
            total_cost += 10
        else:
            print(f"{name}'s ticket price is $15")
            total_cost += 15

print(f"Total Price is ${total_cost}. Hope you enjoy!")

# Exercise 3: ZARA

brand = {
    'name' : 'Zara',
    'creation_date' : 1975,
    'creator_name' : 'Amancio Ortega Gaona',
    'type_of_clothes' : ['men', 'women', 'children', 'home'],
    'international_competitors' : ['Gap', 'H&M', 'Benetton'],
    'number_stores' : 7000,
    'major_color' : {'France' : 'Blue',
                     'Spain' : 'Red',
                     'US' : ['Pink' , 'Green'] 
                    }
}

#a
brand['number_stores'] = 2
#b
print(f"Zara is known for the cheap yet quality clothes that they sell for {brand['type_of_clothes'][0]} and {brand['type_of_clothes'][1]}")
#c
brand.update({'country_creation' : 'Spain'})
print(brand['country_creation'])
#d
for k in brand:
    if k == 'international_competitors':
        brand['international_competitors'].append('Desigual')
#e
del brand['creation_date']
#f
print(brand['international_competitors'][-1])
#g
print(brand['major_color']['US'])
#h
print(len(brand.keys()))
#i
for k in brand.keys():
    print(k)
#Bonus:
more_on_zara = {
    'creation date' : 1975,
    'number_stores' : 2000
}

print(dict(zip(brand,more_on_zara)))

# Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#1
dict_1 = {}
for index in range(len(users)):
    dict_1.update({users[index] : index})
print(dict_1)
# 2
dict_2 = {}
for index in range(len(users)):
    dict_2.update({index : users[index]})
print(dict_2)
# 3
dict_3 = {}
sorted_users = sorted(users)
for index in range(len(sorted_users)):
    dict_3.update({sorted_users[index] : index})
print(dict_3)