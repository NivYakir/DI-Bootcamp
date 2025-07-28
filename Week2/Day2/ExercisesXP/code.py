import random

# Exercise 1: What are you learning?

def display_message() -> str:
    '''Prints a message about what you are learning'''
    print("I am learning about functions in Python.")

display_message()

# Exercise 2: What's your favorite book?

def favorite_book(title) -> str:
    '''Prints the name of your favorite book'''
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

# Exercise 3: Some Geography

def describe_city(city, country= "Unknown"):
    '''Prints the country of the entered City'''
    print(f"{city} is in {country}.")

describe_city("Paris")
describe_city("Reykjavik", "Iceland")

# Exercise 4: Random

def random_number(num) -> str:
    '''Can you correctly guess a number betweeen 1 and 100?'''
    if num in range(1,101):
        x = random.randint(1,100)
        if num == x:
            print("Success!")
        else:
            print("Fail!")
            print(f"The Random Number was {x} and yours was {num}")
    else:
        print("Invalid Number")

random_number(10)

# Exercise 5: Let's Create Some Personalized Shirts

def make_shirt(size = 'Large', message = 'I love Python') -> str:
    '''Describes a shirt size and message'''
    print(f"Shirt Size: {size}")
    print(f"Shirt Message: {message}")

make_shirt()
make_shirt('Medium')
make_shirt('Small','Python is Cool')
make_shirt(message='Python is Fun', size='XL')


# Exercise 6: Magicians

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def make_great(magician_names):
    '''Adds 'the Great' to the end of each name'''
    for i, name in enumerate(magician_names):
        magician_names[i] = name + " " + 'the Great'


def show_magicians(magician_names) -> str:
    '''Prints the names of the magicians in a list'''
    for name in magician_names:
        print(name)

make_great(magician_names)
show_magicians(magician_names)

# Exercise 7: Tempurature Advice

def get_random_temp() -> float:
    '''Enter a month number to receive the current tempurate in Celcius'''
    while True:
        try:
            month = int(input("Enter a month (1-12):\n"))
            if 1 <= month <= 12:
                break
            else:
                print("Month must be between 1 and 12.")
        except ValueError:
            print("Please enter a valid number.")

    if month > 2 and month <= 5:
        temp = random.uniform(10, 30)
    elif month > 5 and month <= 8:
        temp = random.uniform(30, 40)
    elif month > 8 and month <= 11:
        temp = random.uniform(10, 30)
    elif month == 12 or month == 1 or month == 2:
        temp = random.uniform(-10, 10)
    else:
        print("Invalid Month")
    rounded = round(temp, 2)
    return rounded

def main():
    my_temp = get_random_temp()
    print(f"The tempurature right now is {my_temp} degrees Celcius.")
    if my_temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif my_temp >= 0 and my_temp <= 16:
        print("Quite chilly! Don't forget your coat!")
    elif my_temp > 16 and my_temp <= 23:
        print("Nice weather.")
    elif my_temp > 23 and my_temp <= 32:
        print("A bit warm, stay hydrated!")
    else:
        print("It's really hot! Stay cool.")
        
main()