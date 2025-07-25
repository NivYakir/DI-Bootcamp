# Dictionaries
# Syntax: {'key' : 'value' , 'key' : value}

dict_constructor = {
    'name' : 'Juliana',
    'age' : 35,
    'pets' : ['Caramelo', 'Pipoca']
}

user_info = {
    'first_name' : 'Harry',
    'last_name' : 'Potter',
    'age' : 14,
    'address' : 'Privet Drive, 4',
    'pets' : ['Hedwig', 'Buckbeak'],
    'houses' : {'main' : 'Griffyndor' , 'secondary' : 'Slytherin'},
    'best_friends' : ('Ron Weasly' , 'Hermione Granger')
}

# Accessing Data
print(user_info['last_name']) # Potter
print(user_info['houses']) # {'main' : 'Griffyndor' , 'secondary' : 'Slytherin'}

print(user_info['pets'][1]) # Buckbeak
user_info['pets'].append('Pheonix')
print(user_info['pets']) # ['Hedwig', 'Buckbeak', 'Pheonix']
print(user_info['first_name'].upper()) # HARRY

# Changing Values in the dict
user_info['address'] = 'Hogwarts'
print(user_info['address'])

# Deleting a Key
del user_info['age']
print(user_info) # Age is now missing 

# Creating Key Value
user_info['teachers'] = {'Dumbeldore', 'Snape', 'McGonogal'}
print(user_info)

# Exercise 1:
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

# print(sample_dict['class']['student']['marks']['history'])

# Loops and built-in Methods for Dictionaries

# keys()

for k in user_info.keys():
    print(k)

# values()

for v in user_info.values():
    print(v)

# items()
for key, value in user_info.items():
    print(key, value)

for kv_pair in user_info.items():
    print(kv_pair)

# update() Method - adds another key,value to the dict

user_info.update({'patronum' : 'stag'}) # a more clear way of creating a new key,value
print(user_info)

# Exercise 2
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    if key in sample_dict:
        del sample_dict[key]
print(sample_dict)

names = ['Juliana', 'Yosef', 'Sonia']
addresses = ['Ramat Gan', 'Jerusalem', 'Tel Aviv']

print(list(zip(names, addresses)))

topics = ['Math', 'Grammar', 'History', 'Sport']
grades = [85, 90, 100, 75, 87, 55, 25]

print(dict(zip(topics, grades)))