# # Exercise 1: Formula
import math
import statistics

# C = 50
# H = 30

# user_input = input("Please enter a string of numbers separated by a comma: ")
# D_values = user_input.split(',')
# result = []
# for d in D_values:
#     d = int(d)
#     Q = math.sqrt((2 * C * d) / H)
#     result.append(int(Q))

# print(result)

# Exercise 2: List of Integers

list_1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
list_2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
list_3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
list_4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# a:
print(list_1 + list_2 + list_3 + list_4)
# b:
print(sorted(list_1, reverse=True)) 
print(sorted(list_2, reverse=True))
print(sorted(list_3, reverse=True)) 
print(sorted(list_4, reverse=True))
# c:
print(sum(list_1 + list_2 + list_3 + list_4))
# d:
full_list = [list_1, list_2, list_3, list_4]
first_last = []
for lst in full_list:
    first_last.append([lst[0],lst[-1]])
print(first_last)
# e:
one_list = list_1 + list_2 + list_3 + list_4
greater_than_50 = []
for num in one_list:
    if num > 50:
        greater_than_50.append(num)
print(greater_than_50)
# f:
less_than_10 = []
for num in one_list:
    if num < 10:
        less_than_10.append(num)
print(less_than_10)
# g:
squared_list = []
for num in one_list:
    squared_list.append(num ** 2)
print(one_list)
print(squared_list)
# h:
unique_list = set(one_list)
print(unique_list)
print(len(unique_list))
# i:
combined = list_1 + list_2 + list_3 + list_4
print(statistics.mean(combined))
