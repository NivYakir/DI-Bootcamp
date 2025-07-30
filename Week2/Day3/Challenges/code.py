import math

#1 
my_list = ['*','*','*','*','*','*','*',]

def put_in():
    item = 'banana'
    while True:
        try:
            user_i = int(input("Where do you wish to insert? "))
            if user_i in range(0, len(my_list)):
                my_list[user_i] = item
                break
            else:
                print("Invalid Index")
        except ValueError:
            print(f"Invalid Input")
    return my_list

#2
my_sent = "Today was a very hot day. There were way too many birds outside."

def space_count(my_sent):
    counter = 0
    for char in my_sent:
        if char == ' ':
            counter += 1
    return counter

# 3
my_string = 'Good Day Sir. How Are You today'

def char_count(my_string):
    lower = 0
    upper = 0
    for char in my_string:
        if char.isalpha() == True:
            if char.isupper() == True:
                upper += 1
            else:
                lower +=1
    print(f"Lower: {lower}\nUpper: {upper}")

# 4
array = [4,4,2]

def my_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total


# 5
def get_max(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

# 6
def factorial(num):
    result = 1
    counter = num
    while counter != 0:
        result *= counter
        counter -= 1
    return result

# 7

my_list = ['a','b','b','c', 12, True, 'b', 12]

def get_count(list=my_list, check=12):
    counter = 0
    for item in list:
        if item == check:
            counter += 1
    return counter

# 8

def l2_norm(array):
    list_sum = 0
    for num in array:
        num_sqaured = 0
        num_sqaured = num ** 2
        list_sum += num_sqaured
    return int(math.sqrt(list_sum))

print(l2_norm(array))

# 9

