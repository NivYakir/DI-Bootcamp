# Exercise 1: Hello World-I love Python

print(("Hello World \n"*4) + ("I love python \n"*4))

# Exercise 2: What is the season?

month = input("What month is it? Please input a number from 1 to 12: ")
month = int(month)
if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Autumn")
elif month == 12 or month <= 2:
    print("Winter")
else:
    print("Invalid Month")