# Write a script that inserts an item at a defined index in a list.
my_list = ['', '', '', '', '', '']
def insert_item(item, index):
    my_list[index] = item
    print(f"{item} inserted!")

# Write a script that counts the number of spaces in a string.
my_string = 'toDay was A very Nice dAAy for a waKk  .  '
def space_counter(string):
    return string.count(" ")


# Write a script that calculates the number of upper case letters and lower case letters in a string.
def case_count(s):
    return f"Upper: {sum(c.isupper() for c in s)}\nLower: {sum(c.islower() for c in s)}"

# Write a function to find the sum of an array without using the built in function:
my_array = [1,5,4,2]
def my_sum(array):
    result = 0
    for num in array:
        result += num
    
    return result