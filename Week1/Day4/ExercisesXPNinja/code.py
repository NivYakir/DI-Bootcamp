import math
import statistics
import random

# Exercise 1: Formula

C = 50
H = 30

user_input = input("Please enter a string of numbers separated by a comma: ")
D_values = user_input.split(',')
result = []
for d in D_values:
    d = int(d)
    Q = round(math.sqrt((2 * C * d) / H))
    result.append(Q)

print(*result , sep=',')

# Exercise 2: List Of Integers

numbers_1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
numbers_2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
numbers_3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
numbers_4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# # 1
all_numbers = numbers_1 + numbers_2 + numbers_3 + numbers_4

# 2a 
print(all_numbers)

# 2b
all_numbers_sorted_reverse = sorted(all_numbers, reverse=True)
print(all_numbers_sorted_reverse)

# 2c 
print(sum(all_numbers))

# 3
first_and_last = [all_numbers[0], all_numbers[-1]]
print(first_and_last)

# 4 
greater_than_50 = list((num for num in all_numbers if num > 50))
print(greater_than_50)

# 5
smaller_than_10 = list(num for num in all_numbers if num < 10)
print(smaller_than_10)

# 6 
squared_numbers = list(round(math.sqrt(num)) for num in all_numbers if num > 0)
print(squared_numbers)

# 7
all_numbers_no_duplicates = set(all_numbers)
all_numbers_no_duplicates = list(all_numbers_no_duplicates)
print(all_numbers_no_duplicates)

# 8
average = round(sum(all_numbers) / len(all_numbers))
print(average)

# 9
print(max(all_numbers))

# 10
print(min(all_numbers))

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

# 12 Bonus

counter = 0
attempts = 10
num_list = []
while counter < 10:
    user_input = int(input(f"Please enter a number between -100 and 100. You need to enter {attempts} more: "))
    if user_input > 100 or user_input < -100:
        print("You have entered an invalid number!")
        continue
    else:
        num_list.append(user_input)
        counter += 1
        attempts -= 1
print(num_list)

# 13 Bonus

rand_list = []
for num in range(10):
    num = random.randint(-100,100)
    rand_list.append(num)
print(rand_list)

# 14 Bonus

rand_list = []
for num in range(random.randint(0,100)):
    num = random.randint(50, 1000)
    rand_list.append(num)

print(rand_list)

# Exercise 3: Working on a Paragraph

my_paragraph = """𝘵𝘩𝘦 𝘓𝘢𝘥𝘺 𝘔𝘦𝘭𝘪𝘴𝘢𝘯𝘥𝘳𝘦 𝘣𝘪𝘥 𝘮𝘦 𝘨𝘢𝘻𝘦 𝘪𝘯𝘵𝘰 𝘵𝘩𝘦 𝘩𝘦𝘢𝘳𝘵𝘩𝘧𝘪𝘳𝘦. 𝘛𝘩𝘦 𝘤𝘩𝘪𝘮𝘯𝘦𝘺 𝘸𝘢𝘴 𝘥𝘳𝘢𝘸𝘪𝘯𝘨 𝘴𝘵𝘳𝘰𝘯𝘨𝘭𝘺, 𝘢𝘯𝘥 𝘣𝘪𝘵𝘴 𝘰𝘧 𝘢𝘴𝘩 𝘸𝘦𝘳𝘦 𝘳𝘪𝘴𝘪𝘯𝘨 𝘧𝘳𝘰𝘮 𝘵𝘩𝘦 𝘧𝘪𝘳𝘦. 
                𝘐 𝘴𝘵𝘢𝘳𝘦𝘥 𝘢𝘵 𝘵𝘩𝘦𝘮, 𝘧𝘦𝘦𝘭𝘪𝘯𝘨 𝘩𝘢𝘭𝘧 𝘢 𝘧𝘰𝘰𝘭, 𝘣𝘶𝘵 𝘴𝘩𝘦 𝘣𝘪𝘥 𝘮𝘦 𝘭𝘰𝘰𝘬 𝘥𝘦𝘦𝘱𝘦𝘳, 𝘢𝘯𝘥 𝘵𝘩𝘦 𝘢𝘴𝘩𝘦𝘴 𝘸𝘦𝘳𝘦 𝘸𝘩𝘪𝘵𝘦, 𝘳𝘪𝘴𝘪𝘯𝘨 𝘪𝘯 𝘵𝘩𝘦 𝘶𝘱𝘥𝘳𝘢𝘧𝘵, 𝘺𝘦𝘵 𝘢𝘭𝘭 𝘢𝘵 𝘰𝘯𝘤𝘦 𝘪𝘵 𝘴𝘦𝘦𝘮𝘦𝘥 
                𝘢𝘴 𝘪𝘧 𝘵𝘩𝘦𝘺 𝘸𝘦𝘳𝘦 𝘧𝘢𝘭𝘭𝘪𝘯𝘨. 𝘚𝘯𝘰𝘸, 𝘐 𝘵𝘩𝘰𝘶𝘨𝘩𝘵. 𝘛𝘩𝘦𝘯 𝘵𝘩𝘦 𝘴𝘱𝘢𝘳𝘬𝘴 𝘪𝘯 𝘵𝘩𝘦 𝘢𝘪𝘳 𝘴𝘦𝘦𝘮𝘦𝘥 𝘵𝘰 𝘤𝘪𝘳𝘤𝘭𝘦, 𝘵𝘰 𝘣𝘦𝘤𝘰𝘮𝘦 𝘢 𝘳𝘪𝘯𝘨 𝘰𝘧 𝘵𝘰𝘳𝘤𝘩𝘦𝘴, 𝘢𝘯𝘥 𝘐 𝘸𝘢𝘴 𝘭𝘰𝘰𝘬𝘪𝘯𝘨 𝘵𝘩𝘳𝘰𝘶𝘨𝘩 
                𝘵𝘩𝘦 𝘧𝘪𝘳𝘦 𝘥𝘰𝘸𝘯 𝘰𝘯 𝘴𝘰𝘮𝘦 𝘩𝘪𝘨𝘩 𝘩𝘪𝘭𝘭 𝘪𝘯 𝘢 𝘧𝘰𝘳𝘦𝘴𝘵. 𝘛𝘩𝘦 𝘤𝘪𝘯𝘥𝘦𝘳𝘴 𝘩𝘢𝘥 𝘣𝘦𝘤𝘰𝘮𝘦 𝘮𝘦𝘯 𝘪𝘯 𝘣𝘭𝘢𝘤𝘬 𝘣𝘦𝘩𝘪𝘯𝘥 𝘵𝘩𝘦 𝘵𝘰𝘳𝘤𝘩𝘦𝘴, 𝘢𝘯𝘥 𝘵𝘩𝘦𝘳𝘦 𝘸𝘦𝘳𝘦 𝘴𝘩𝘢𝘱𝘦𝘴 𝘮𝘰𝘷𝘪𝘯𝘨 𝘵𝘩𝘳𝘰𝘶𝘨𝘩 𝘵𝘩𝘦 𝘴𝘯𝘰𝘸. 
                𝘍𝘰𝘳 𝘢𝘭𝘭 𝘵𝘩𝘦 𝘩𝘦𝘢𝘵 𝘰𝘧 𝘵𝘩𝘦 𝘧𝘪𝘳𝘦, 𝘐 𝘧𝘦𝘭𝘵 𝘢 𝘤𝘰𝘭𝘥 𝘴𝘰 𝘵𝘦𝘳𝘳𝘪𝘣𝘭𝘦 𝘐 𝘴𝘩𝘪𝘷𝘦𝘳𝘦𝘥, 𝘢𝘯𝘥 𝘸𝘩𝘦𝘯 𝘐 𝘥𝘪𝘥 𝘵𝘩𝘦 𝘴𝘪𝘨𝘩𝘵 𝘸𝘢𝘴 𝘨𝘰𝘯𝘦, 𝘵𝘩𝘦 𝘧𝘪𝘳𝘦 𝘣𝘶𝘵 𝘢 𝘧𝘪𝘳𝘦 𝘰𝘯𝘤𝘦 𝘢𝘨𝘢𝘪𝘯. 
                𝘉𝘶𝘵 𝘸𝘩𝘢𝘵 𝘐 𝘴𝘢𝘸 𝘸𝘢𝘴 𝘳𝘦𝘢𝘭, 𝘐'𝘥 𝘴𝘵𝘢𝘬𝘦 𝘮𝘺 𝘬𝘪𝘯𝘨𝘥𝘰𝘮 𝘰𝘯 𝘪𝘵."""

print(f"This paragraph contains {len(my_paragraph)} characters.")
print(f"This paragraph contains {my_paragraph.count('.')} sentences.")
print(f"This paragraph contains {my_paragraph.count(' ') + 1} words.")
paralist = my_paragraph.split()
print(f"This paragraph contains {len(paralist)} unique words.")

# Exercise 4: Frequency of Words

user_input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

words = user_input.split()
for word in set(words):
    print(f"{word} : {words.count(word)}")