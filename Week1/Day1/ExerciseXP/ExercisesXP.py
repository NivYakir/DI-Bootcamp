# Exercise 1: Hello World - Print the following output in one line of code:

print("Hello World \nHello World \nHello World \nHello World")

# Exercise 2: Some Math - Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8)

print((99 ** 3) * 8)

# Exercise 3: What is the Output

False
True
False
False
False

# Exerice 4: Your Computer Brand

computer_brand = "Asus"
print(f"I have a {computer_brand} computer")

# Exercise 5: Your Information

name = "Niv"
age = 30
shoe_size = 43
info = f"Hello, my name is {name}. I am {age} years old and I have a shoe size of {shoe_size}."
print(info)

# Exercise 6: A & B
a = 15
b = 16
if a > b:
    print("Hello World")

# Exericse 7: Odd or Even

my_num = input("Please enter a number: ")
my_num = int(my_num)
if my_num % 2 == 0:
    print("The number you chose is Even")
else:
    print("The number you chose is Odd")

# Exercise 8: What's Your Name?

my_name = "Niv"
user_name = input("What is your name: ")
if my_name == user_name:
    print("Holy cow! We have the same name!")
else:
    print("Wow, you have a repulsive name and you parents should be ashamed!")

# Exercise 9: Tall enough to ride a rollercoaster

user_height = input("What is your height in centimeters? ")
user_height = int(user_height)
min_height = 145
if user_height > min_height:
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")
