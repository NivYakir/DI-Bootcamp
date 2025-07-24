# List: An ordered sequence of elements that can be changed (mutable).

user_name = 'niv'
email = 'niv@gmail.com'
user_age = 30
is_online = True

user_info = [user_name, email, user_age, is_online]
print(len(user_info)) # 4

# every structure in python has a builder as follows:

some_list = list('item 1') # create a list with a function
other_list = ['item 1', 'item 2']

print(some_list) # ['i','t','e','m','1']
print(other_list) # ['item 1', 'item 2']

empty_list = [] # the basis for creating any list
print(user_info[2]) # prints user_age element (user_age is in index #2)

fruits = ['orange', 'lemon', 'apple', 'kiwi']
# slice
print(fruits[-2:]) # ['apple', 'kiwi']

fruits[1] = 'pineapple' # changes the element at index 1 from 'lemon' to 'pineapple'
print(fruits) # ['orange', 'pineapple', 'apple', 'kiwi']

# List Methods: A method is a 'function' that is used for a specific class/object
fruits = ['orange', 'lemon', 'apple', 'kiwi']

fruits.insert(1, 'banana')
#print(fruits) #['orange', 'banana', 'lemon', 'apple', 'kiwi']

fruits.remove('kiwi') # removes the 1st appearance of element 'kiwi'
#print(fruits)

fruits.append('watermelon') # adds specified element to the end of the list
#print(fruits)

fruits.pop(1) # removes final element (if no argument), else removes element at specified index
#print(fruits)

veggies = ['tomato', 'potato', 'carrot']
fruits.extend(veggies) # adds the elements in the list, to the original list
#print(fruits)

# sorted() and .sort()
fruits_sorted = sorted(fruits)
print(fruits)
print(fruits_sorted)

fruits.sort()
print(fruits)

# List Exercise

list1 = [5, 10, 15, 20, 25, 50, 20]

if 20 in list1:
    index_20 = list1.index(20)
    list1[index_20] = 200
print(list1)

# While Loops

i = 0
while i < len(fruits):
    print(i)
    i += 1
