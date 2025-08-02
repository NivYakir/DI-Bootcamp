# # import random

# # # # Timed Challenge: Functions

# # # def count_occurence():
# # #     my_string = input("Enter a string:\n")
# # #     check = input("Enter a letter:\n")
# # #     counter = 0
# # #     for char in my_string:
# # #         if char == check:
# # #             counter += 1
# # #     return counter

# # # print(count_occurence())

# # # my_string = 'Tommorow yesterday was today'
# # # print(list(my_string))

# # # def count_occurence_2():
# # #     my_string = input("Enter a string:\n")
# # #     check = input("Enter a letter:\n")
# # #     temp = list(my_string)
# # #     return temp.count(check)

# # # print(count_occurence())

# # # # Exercise 1: Sum

# # # def get_sum(x):
# # #     result = []
# # #     for num in range(1,5):
# # #         my_str = ""
# # #         my_str += (num * x)
# # #         my_num = int(my_str)
# # #         result.append(my_num)
# # #     return sum(result)

# # # print(get_sum('3'))

# # # # Exercise 2: Double Dice

# # # def throw_dice():
# # #     '''Returns a number between 1 and 6'''
# # #     return random.randint(1,6)

# # # def throw_until_doubles():
# # #     counter = 0
# # #     while True:
# # #         roll_1 = throw_dice()
# # #         roll_2 = throw_dice()
# # #         counter += 1
# # #         if roll_1 == roll_2:
# # #             break
# # #     return counter

# # # def main():
# # #     result = []
# # #     for _ in range(100):
# # #         result.append(throw_until_doubles())
# # #     print(result)
# # #     return sum(result)

# # # print(main())

# # # my_string = input(f"Enter a string:\n")
# # # result = {}
# # # for i, char in enumerate(my_string):
# # #     if char not in result.keys():
# # #         result.update({char : [i]})
# # #     else:
# # #         result[char].append(i)

# # # print(result)


# # MATRIX_STR = '''7ii
# # Tsx
# # h%?
# # i #
# # sM 
# # $a 
# # #t%'''


# # def string_to_matrix(text):
# #     '''Converts a string to a 2D Matrix'''
# #     result = []
# #     temp = text.split('\n')
# #     for row in temp:
# #         rows = []
# #         for char in row:
# #             rows.append(char)
# #         result.append(rows)
# #     return result

# # print(string_to_matrix(MATRIX_STR))

# # def matrix_decode():
# #     result = ''
# #     matrix = string_to_matrix(MATRIX_STR)
# #     rows = len(matrix)
# #     columns = len(matrix[0])

# #     for c in range(columns):
# #         for r in range(rows):
# #             letter = matrix[r][c]
# #             if letter.isalpha() == True:
# #                 result += letter
# #     print(result)

# # matrix_decode()

# # board = [[" " for cells in range(3)] for cells in range(3)]

# # print(board)





# # my_word = 'pytthon'
# # my_board = ['*' for char in my_word]
# # user_input = 't'

# # for i in range(len(my_board)):
# #     if user_input == my_word[i]:
# #         my_board[i] = user_input
# # print(my_board)

# word = 'pythagarusursu'
# board = ['g' for char in word]
# guessed_letters = []

# def display_gallows(attempt):
#     '''Displays the hangman's status'''
#     board_stage = ["""
#             -------
#             |  O  |
#             | /|\\ |
#             | / \\ |
#             -------
#     """,
#         """
#             -------
#             |  O  |
#             | /|\\ |
#             | /   |
#             -------
#     """,
#     """
#             -------
#             |  O  |
#             | /|\\ |
#             |     |
#             -------
#     """,
#     """
#             -------
#             |  O  |
#             | /|  |
#             |     |
#             -------
#     """,
#     """
#             -------
#             |  O  |
#             |  |  |
#             |     |
#             -------
#     """,
#     """
#             -------
#             |  O  |
#             |     |
#             |     |
#             -------
#     """,
#     """
#             -------
#             |     |
#             |     |
#             |     |
#             -------
#     """]

#     print(board_stage[attempt])

# def letter_check(board,word,guessed_letters):
#     attempt = 6
#     while True:
#         user_input = input("Guess a letter: ").lower()
#         print(user_input)
#         if len(user_input) == 1 and (user_input.isalpha() == True):
#             if user_input in guessed_letters:
#                 print("You have already guessed this letter")
#             else: 
#                 if user_input in word:
#                     for i in range(len(board)):
#                         if user_input == word[i]:
#                             board[i] = user_input
#                             guessed_letters.append(user_input)
#                     break
#                 else:
#                     guessed_letters.append(user_input)
#                     attempt -= 1
#                     display_gallows(attempt)
#                     break
#         else:
#             print("Invalid input.")
#     print(board)

# def win_check(board):
#     '''Returns True if all the letters have been guessed correctly'''
#     if '*' in board:
#         return False
#     else:
#         return True


# print(win_check(board))

# player = 2

# def true_or_false():
#     if player == 1:
#         return True
#     else:
#         return False
    

# attempt = 0
# while attempt != 6:
#     if true_or_false == True:
#         print('Okay')
#     else:
#         print('Not okay')
#         attempt += 1



# board = [[" " for row in range(3)] for cell in range(3)]
# print(board)

# for i in range(3):
#     if board[i][0] == board[i][1] == board[i][2] != " " :
#         print("True")
#     elif board[0][i] == board[1][i] == board[2][i] != " ":
#         print("True")
# if board[0][0] == board[1][1] == board[2,2] != " " :
#     print("True")
# elif board[0][2] == board[1][1] == board[2][0] != " " :
#     print("True")
# else:
#     print("false")



# my_list = ['*','*','*','*','*','*','*','*']

# def put_in(index=int, thelist=my_list):
#     item = 'apple'
#     thelist[index] = item
#     return thelist




# my_array = [7,6,5,5,2,0]


# def is_mono(array):
#     asc_count = 1
#     dsc_count = 1
#     for i in range(1, len(array)):
#         if array[i] < array[i - 1]:
#             dsc_count += 1
#         elif array[i] > array[i - 1]:
#             asc_count += 1
#         elif array[i] == array[i - 1]:
#             asc_count += 1
#             dsc_count += 1
    
#     if asc_count == len(array) or dsc_count == len(array):
#         return True
#     else:
#         return False


def is_mono(array):
    asc = True
    dsc = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            dsc = False
        elif array[i] < array[i - 1]:
            asc = False
    
    return asc or dsc

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))