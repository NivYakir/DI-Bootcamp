import math
import statistics

# # Exercise 1: Formula

# C = 50
# H = 30

# user_input = input("Please enter a string of numbers separated by a comma: ")
# D_values = user_input.split(',')
# result = []
# for d in D_values:
#     d = int(d)
#     Q = round(math.sqrt((2 * C * d) / H))
#     result.append(Q)

# print(*result , sep=',')

# # Exercise 2: List Of Integers

numbers_1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
numbers_2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
numbers_3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
numbers_4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# # 1
all_numbers = numbers_1 + numbers_2 + numbers_3 + numbers_4

# # 2a 
# print(all_numbers)

# # 2b
# all_numbers_sorted_reverse = sorted(all_numbers, reverse=True)
# print(all_numbers_sorted_reverse)

# # 2c 
# print(sum(all_numbers))

# # 3
# first_and_last = [all_numbers[0], all_numbers[-1]]
# print(first_and_last)

# # 4 
# greater_than_50 = list((num for num in all_numbers if num > 50))
# print(greater_than_50)

# # 5
# smaller_than_10 = list(num for num in all_numbers if num < 10)
# print(smaller_than_10)

# # 6 
# squared_numbers = list(round(math.sqrt(num)) for num in all_numbers if num > 0)
# print(squared_numbers)

# # 7
# all_numbers_no_duplicates = set(all_numbers)
# all_numbers_no_duplicates = list(all_numbers_no_duplicates)
# print(all_numbers_no_duplicates)

# # 8
# average = round(sum(all_numbers) / len(all_numbers))
# print(average)

# # 9
# print(max(all_numbers))

# # 10
# print(min(all_numbers))

# Bonus
# 11

sum_nums = 0
for num in all_numbers:
    sum_nums += num
print(sum_nums)

print(sum_nums / len(all_numbers))

largest_number = all_numbers[0]
for num in all_numbers:
    if num > largest_number:
        largest_number = num
print(largest_number)

smallest_number = all_numbers[0]
for num in all_numbers:
    if num < smallest_number:
        smallest_number = num
print(smallest_number)

