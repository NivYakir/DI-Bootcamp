import random

# Exercise 1: When Will I Retire?

def get_age(year, month, day):
    current_year = 2025
    current_month = 7
    current_day = 28
    age = current_year - year
    if (current_month, current_day) < (month, day):
        age -= 1
    return age

def can_retire(gender, date_of_birth):
    year, month, day = date_of_birth.split('/')
    year, month, day = int(year), int(month), int(day)
    my_age = get_age(year, month, day)
    if gender == 'f':
        if my_age >= 62:
            print("You can retire!")
            return True
        else:
            print("You can't retire.")
    elif gender == 'm':
        if my_age >= 67:
            print("You can retire!")
            return True
        else:
            print("You can't retire.")
            return False
    else:
        print("Please enter 'm or f'")

can_retire('f','1967/10/12')

# Exercise 2: Sum

def get_sum(x):
    result = []
    for num in range(1, 5):
        my_str = ""
        my_str += x*num
        my_num = int(my_str)
        result.append(my_num)
    return sum(result)

print(get_sum('3'))

# Exercise 3: Double Dice

def throw_dice():
    '''Returns a number between 1 and 6'''
    return random.randint(1,6)

def throw_until_double():
    '''Returns the number of attempts it took to roll a double'''
    roll_count = 0
    while True:
        roll_1 = throw_dice()
        roll_2 = throw_dice()
        roll_count += 1
        if roll_1 == roll_2:
            break
    return roll_count

def main():
    '''Returns the number and avg number of attempts it took reach 100 doubles'''
    result = {}
    total_throws = 0
    for i in range(100):
        roll = throw_dice()
        total_throws += roll
        result.update({i : roll})
    print(f"Total Throws: {total_throws}")
    print(f"Average Throws to Reach Double: {round((total_throws / 100), 2)}")
    return result

main()

# Exercise 2 (dynamix solution)

def get_sum():
    x = input("Enter a number (1-9):\n")
    y = int(input("Enter another one: "))
    result = []
    for y in range(1, y + 1):
        my_str = ""
        my_str += (x * y)
        my_num = int(my_str)
        result.append(my_num)
    return sum(result)

print(get_sum())