# import random

# # # Timed Challenge: Functions

# # def count_occurence():
# #     my_string = input("Enter a string:\n")
# #     check = input("Enter a letter:\n")
# #     counter = 0
# #     for char in my_string:
# #         if char == check:
# #             counter += 1
# #     return counter

# # print(count_occurence())

# # my_string = 'Tommorow yesterday was today'
# # print(list(my_string))

# # def count_occurence_2():
# #     my_string = input("Enter a string:\n")
# #     check = input("Enter a letter:\n")
# #     temp = list(my_string)
# #     return temp.count(check)

# # print(count_occurence())

# # # Exercise 1: Sum

# # def get_sum(x):
# #     result = []
# #     for num in range(1,5):
# #         my_str = ""
# #         my_str += (num * x)
# #         my_num = int(my_str)
# #         result.append(my_num)
# #     return sum(result)

# # print(get_sum('3'))

# # # Exercise 2: Double Dice

# # def throw_dice():
# #     '''Returns a number between 1 and 6'''
# #     return random.randint(1,6)

# # def throw_until_doubles():
# #     counter = 0
# #     while True:
# #         roll_1 = throw_dice()
# #         roll_2 = throw_dice()
# #         counter += 1
# #         if roll_1 == roll_2:
# #             break
# #     return counter

# # def main():
# #     result = []
# #     for _ in range(100):
# #         result.append(throw_until_doubles())
# #     print(result)
# #     return sum(result)

# # print(main())

# # my_string = input(f"Enter a string:\n")
# # result = {}
# # for i, char in enumerate(my_string):
# #     if char not in result.keys():
# #         result.update({char : [i]})
# #     else:
# #         result[char].append(i)

# # print(result)


# MATRIX_STR = '''7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%'''


# def string_to_matrix(text):
#     '''Converts a string to a 2D Matrix'''
#     result = []
#     temp = text.split('\n')
#     for row in temp:
#         rows = []
#         for char in row:
#             rows.append(char)
#         result.append(rows)
#     return result

# print(string_to_matrix(MATRIX_STR))

def matrix_decode():
    result = ''
    matrix = string_to_matrix(MATRIX_STR)
    rows = len(matrix)
    columns = len(matrix[0])

    for c in range(columns):
        for r in range(rows):
            letter = matrix[r][c]
            if letter.isalpha() == True:
                result += letter
    print(result)

matrix_decode()

board = [[" " for cells in range(3)] for cells in range(3)]

print(board)