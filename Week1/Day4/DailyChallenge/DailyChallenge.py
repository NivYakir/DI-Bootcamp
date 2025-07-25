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

my_string = list(input("Please enter a string of your choice:\n"))
dup_check = []

for char in my_string:
    if char not in dup_check:
        dup_check.append(char)
result = ''.join(dup_check)
print(result)