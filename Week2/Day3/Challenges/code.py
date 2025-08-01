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
    for i in range(2, num + 1):
        result *= i
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
        list_sum += (num ** 2)
    return int(math.sqrt(list_sum))

print(l2_norm([1,2,2]))

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
def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

# 17
my_nums = [1,2,2,3,4,5]

def even_nums(numlist):
    result = []
    for i, num in enumerate(numlist):
        if i % 2 == 0 and num % 2 == 0:
            result.append(num)
    return result

# 18

def type_count(**kwargs):
    int_count = 0
    str_count = 0
    float_count = 0
    bool_count = 0
    for t in kwargs.values():
        if type(t) == int:
            int_count += 1
        elif type(t) == str:
            str_count += 1
        elif type(t) == float:
            float_count += 1
        else:
            bool_count +=1

    return f"int: {int_count}, str: {str_count}, float: {float_count}, bool: {bool_count}"

# 19
my_sentence = 'today/there/was/a/big/ass/bird/outside/and/it made/me cry   '

def splitter(text, char=' '):
    result = []
    temp = ''
    for letter in text:
        if letter != char:
            temp += letter
        else:
            result.append(temp)
            temp = ''
    if text[-1] != char:
        result.append(temp)
    return result

# 20
my_pass = 'password123'

def password(password):
    result = ''.join('*' for char in password)
    return result