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
# array = [4,4,2]

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

# 10
my_list = ['a',101,2,'there',5,'was',10,12,'continuous','traffic']

def get_longest(word_list):
    longest = ''
    for word in word_list:
        if len(word) > len(longest):
            longest = word     
    print(longest)

# 11

def separate(a_list):
    num_list = []
    str_list = []
    for item in a_list:
        if type(item) == int:
            num_list.append(item)
        else:
            str_list.append(item)
    return num_list, str_list

# 12

my_string = 'titties'

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
# 13
my_sentence = 'today there was a big ass bird outside and it made me cry'

def sum_over_k(k, sentence):
    temp = sentence.split(" ")
    counter = 0
    for word in temp:
        if len(word) >= k:
            counter += 1
    return counter

# 14
my_dict = {'a': 8,'b':8,'c':8,'d': 8}

def dict_avg(dict):
    temp = 0
    for num in my_dict.values():
        temp += num
    result = temp / len(dict)
    return result

# 15

def com_divs(num1,num2):
    result = []
    my_num = 0
    if num1 < num2:
        my_num = num1
    else:
        my_num = num2
    
    for num in range(2,my_num + 1):
        if round(my_num/num) == my_num/num:
    #   if num1 % num == 0 and num2 % num == 0: <-- (better version)
            result.append(num)
    return result

# 16

