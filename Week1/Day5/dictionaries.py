# # Dictionaries
# # Syntax: {'key' : 'value' , 'key' : value}

# dict_constructor = {
#     'name' : 'Juliana',
#     'age' : 35,
#     'pets' : ['Caramelo', 'Pipoca']
# }

# user_info = {
#     'first_name' : 'Harry',
#     'last_name' : 'Potter',
#     'age' : 14,
#     'address' : 'Privet Drive, 4',
#     'pets' : ['Hedwig', 'Buckbeak'],
#     'houses' : {'main' : 'Griffyndor' , 'secondary' : 'Slytherin'},
#     'best_friends' : ('Ron Weasly' , 'Hermione Granger')
# }

# # Accessing Data
# print(user_info['last_name']) # Potter
# print(user_info['houses']) # {'main' : 'Griffyndor' , 'secondary' : 'Slytherin'}

# print(user_info['pets'][1]) # Buckbeak
# user_info['pets'].append('Pheonix')
# print(user_info['pets']) # ['Hedwig', 'Buckbeak', 'Pheonix']
# print(user_info['first_name'].upper()) # HARRY

# # Changing Values in the dict
# user_info['address'] = 'Hogwarts'
# print(user_info['address'])

# # Deleting a Key
# del user_info['age']
# print(user_info) # Age is now missing 

# # Creating Key Value
# user_info['teachers'] = {'Dumbeldore', 'Snape', 'McGonogal'}
# print(user_info)

# # Exercise 1:
# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# # print(sample_dict['class']['student']['marks']['history'])

# # Loops and built-in Methods for Dictionaries

# # keys()

# for k in user_info.keys():
#     print(k)

# # values()

# for v in user_info.values():
#     print(v)

# # items()
# for key, value in user_info.items():
#     print(key, value)

# for kv_pair in user_info.items():
#     print(kv_pair)

# # update() Method - adds another key,value to the dict

# user_info.update({'patronum' : 'stag'}) # a more clear way of creating a new key,value
# print(user_info)

# # Exercise 2
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# keys_to_remove = ["name", "salary"]

# for key in keys_to_remove:
#     if key in sample_dict:
#         del sample_dict[key]
# print(sample_dict)

# names = ['Juliana', 'Yosef', 'Sonia']
# addresses = ['Ramat Gan', 'Jerusalem', 'Tel Aviv']

# print(list(zip(names, addresses)))

# topics = ['Math', 'Grammar', 'History', 'Sport']
# grades = [85, 90, 100, 75, 87, 55, 25]

# print(dict(zip(topics, grades)))


# # # Exercise 2:

# # family = {}
# # total_cost = 0
# # while True:
# #     user_input = input("Please enter (name/age) of family member, or type 'quit' if you are finished.\n")
# #     if user_input.lower() == 'quit':
# #         break
# #     else:
# #         name, age = user_input.split('/')
# #         age = int(age)
# #         family.update({name : age})
# #         if age < 3:
# #             print(f"{name}'s ticket cost is FREE")
# #         elif age >= 3 and age <= 12:
# #             print(f"{name}'s ticket cost is $10")
# #             total_cost += 10
# #         else:
# #             print(f"{name}'s ticket cost is $15")
# #             total_cost += 15
# # print(f"The total cost is ${total_cost}")

# my_string = input("Enter a string\n")
# result = ''

# for i in range(len(my_string)):
#     if i == 0 or my_string[i] != my_string[i - 1]:
#         result += my_string[i]
# print(result)


# # Daily Challenge 1

# my_string = input(f"Enter a string:\n")
# my_dict = {}

# for index, letter in enumerate(my_string):
#     if letter not in my_dict.keys():
#         my_dict[letter] = [index]
#     else:
#         my_dict[letter].append(index)
# print(my_dict)

# # Daily Challenge 2
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"
# my_money = int(wallet.replace("$",""))
# result = []

# for key in items_purchase.keys():
#     cleaned = int(items_purchase[key].replace("$","").replace(",",""))
#     items_purchase[key] = cleaned
#     if my_money > cleaned:
#         result.append(key)

# print(sorted(result))

# #1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# print(dict(zip(keys,values)))

# # 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total_cost = 0

# for name, age in family.items():
#     if age in range(0,2):
#         print(f"{name}'s ticket is FREE")
#     elif age in range(3,12):
#         print(f"{name}'s ticket is $10.")
#         total_cost += 10
#     else:
#         print(f"{name}'s ticket is $15.")
#         total_cost += 15

# # print(f"Total Cost: ${total_cost}")

# # Timed Challenge 1:

# user_input = input(f"Please enter a sentence:\n").replace(".","")
# reversed = user_input.split(' ')[::-1]

# print(*reversed)

# Timed Challenge 2

x = int(input("Enter a number:\n"))
temp = []

for mod_check in range(1, x):
    if x % mod_check == 0:
        temp.append(mod_check)

check = sum(temp)

if x == check:
    print(True)
else:
    print(False)