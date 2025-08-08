import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

# # Converting dict to a file
# with open(f'{dir_path}/family.json', 'w') as f:
#     json.dump(my_family, f)

# # Converting dict to a json string
json_my_family_str = json.dumps(my_family)
# print(json_my_family_str)

# Converting from a json file to a dict
with open(f'{dir_path}/family.json', 'r') as f:
    my_family2 = json.load(f)

print(my_family2) # type dict

# Converting from a json string to a dict
parsed_family = json.loads(json_my_family_str)
print(parsed_family) # type dict