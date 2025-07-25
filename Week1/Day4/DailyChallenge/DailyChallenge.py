# Challenge 1: Multiples of a Number

num_input = int(input("Please enter a number: "))
len_input = int(input("Please enter how many multiples of that number you wish to see: "))
new_num = num_input
my_list = []
for num in range(len_input):
    my_list.append(new_num)
    new_num += num_input

print(my_list)

# Challenge 2: Remove Consecutive Duplicate Letters

my_string = input("Please enter a string: ")
result = ""

for i in range(len(my_string)):
    if i == 0 or my_string[i] != my_string[i - 1]:
        result += my_string[i]
print(result)