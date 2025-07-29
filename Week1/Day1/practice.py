import random

# # Timed Challenge: Functions

# def count_occurence():
#     my_string = input("Enter a string:\n")
#     check = input("Enter a letter:\n")
#     counter = 0
#     for char in my_string:
#         if char == check:
#             counter += 1
#     return counter

# print(count_occurence())

# my_string = 'Tommorow yesterday was today'
# print(list(my_string))

# def count_occurence_2():
#     my_string = input("Enter a string:\n")
#     check = input("Enter a letter:\n")
#     temp = list(my_string)
#     return temp.count(check)

# print(count_occurence())

# # Exercise 1: Sum

# def get_sum(x):
#     result = []
#     for num in range(1,5):
#         my_str = ""
#         my_str += (num * x)
#         my_num = int(my_str)
#         result.append(my_num)
#     return sum(result)

# print(get_sum('3'))

# Exercise 2: Double Dice

def throw_dice():
    '''Returns a number between 1 and 6'''
    return random.randint(1,6)

def throw_until_doubles():
    counter = 0
    while True:
        roll_1 = throw_dice()
        roll_2 = throw_dice()
        counter += 1
        if roll_1 == roll_2:
            break
    return counter

def main():
    result = []
    for _ in range(100):
        result.append(throw_until_doubles())
    print(result)
    return sum(result)

print(main())