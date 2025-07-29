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

print(get_sum('2'))