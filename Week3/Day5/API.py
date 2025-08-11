# API: a set of rules that allows different software applications to communicate and share data with each other.
# Many API's communicate using JSON format
import requests
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

#SYNTAX: response = requests.get('URL')
response = requests.get('https://api.chucknorris.io/jokes/random')

# print(response)  # <Response [200]> *GOOD*   (Response[400] *NOT GOOD*)
# print(response.text) # gives the full JSON response

data = json.loads(response.text) # converts the response into a dictionary

print(data['value']) # access the data dictionary using normal dict syntax

with open(f'{dir_path}/jokes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, sort_keys=True)