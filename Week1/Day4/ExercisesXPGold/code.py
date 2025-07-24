import random

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

num_1 = int(input("Please input the first number: "))
num_2 = int(input("Please input the second number: "))
num_3 = int(input("Please input the third number: "))

all_num = [num_1, num_2, num_3]
print(max(all_num))

# Exercise 5: The Alphabet

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    if letter in ['a','e','i','o','u']:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")

# Exercise 6: Words and Letters

word_input = input("Please enter 7 words separated by a space: ")
words = word_input.split()

if len(words) != 7:
    print("You need to enter exactly 7 words!")
else:
    letter = input("Please enter a letter from the english alphabet: ")

    for word in words:
        if letter in word:
            index = word.find(letter)
            print(index)
        else:
            print(f"Unfortunately, the letter '{letter}' does not appear in the word {word}")

# Exercise 7: Min, Max, Sum

num_list = []
for num in range(1, 1000001):
    num_list.append(int(num))
print(min(num_list))
print(max(num_list))
print(sum(num_list))

# Exercise 8: List and Tuple

num_input = input("Please enter a sequence of numbers, separated by a comma: ")
nums = num_input.split(',')
print(list(nums))
print(tuple(nums))

# Exercise 9: Random Number

win_count = 0
loss_count = 0

while True:
    user_input = input("Enter a number between 1 and 9 (inclusive): ")
    rand_num = random.randint(1,9)
    if user_input.lower() == "quit":
        print(f"You have won {win_count} time(s)")
        print(f"You have lost {loss_count} time(s)")
        break
    elif int(user_input) not in range(1,10):
        print("You have entered an invalid number!")
    else:
        user_input = int(user_input)
        if user_input == rand_num:
            print("Winner!")
            win_count += 1
        else:
            print(f"The number was {rand_num}. Better luck next time!")
            loss_count += 1