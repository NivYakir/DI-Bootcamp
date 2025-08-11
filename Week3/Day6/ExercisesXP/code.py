import os
import json
import random
dir_path = os.path.dirname(os.path.realpath(__file__))

# Exercise 1: Random Sentence Generator

def get_words_from_file(path):
    with open(f'{path}/words.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]

def get_random_sentence(length):
    word_list = get_words_from_file(dir_path)
    result = ' '.join(random.choice(word_list).lower() for _ in range(length)) + '.'
    return result[0].upper() + result[1:]

def main():
    print("This program will print a random sentence of your desired length.")
    while True:
        try:
            length_input = input("Please enter a number between 2 and 20: ")
            length = int(length_input)

            if length > 20 or length < 2:
                print("You must enter an integer between 2 and 20.")
                continue

            result = get_random_sentence(length)
            print(result)
            break
        except ValueError:
            print("Invalid Input. Enter a valid integer.")


# Exercise 2: Working with JSON

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON String
sample = json.loads(sampleJson)

# Step 2: Access the 'salary' key
print(sample["company"]["employee"]["payable"]["salary"])

# Step 3: Add the birth_date key
sample["company"]["employee"]["birth_date"] = "1994-10-10"

# Step 4: Save the JSON to a file
with open(f'{dir_path}/sample.json', 'w', encoding='utf-8') as f:
    json.dump(sample, f, indent=4, sort_keys=True)