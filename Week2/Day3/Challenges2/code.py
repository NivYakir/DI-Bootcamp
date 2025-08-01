# Exercise 1

# a
rows = 5

for i in range(rows):
    spaces = rows - i
    stars = 2 * i + 1
    print(" " * spaces + '*' * stars)

#b
for i in range(rows):
    spaces = rows - (i + 1)
    stars = i + 1
    print(" " * spaces + "*" * stars)

#c
for i in range(rows):
    print('*' * (i + 1))
for i in range(rows):
    stars = rows - i
    spaces = i
    print(" " * spaces + "*" * stars)



# Exercise 2
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)