# Exercise 1: Currency

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"Currency(currency='{self.currency}', amount={self.amount})"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add different currencies. Got {self.currency} and {other.currency}")
            return Currency(self.currency, self.amount + other.amount)
        raise TypeError(f"Unsupported operand type for +: 'Currency' and '{type(other).__name__}'")

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
            return self
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add different currencies. Got {self.currency} and {other.currency}")
            self.amount += other.amount
            return self
        raise TypeError(f"Unsupported operand type for +=: 'Currency' and '{type(other).__name__}'")
    
# Exercise 2: Import

import func
func.adding(3,8)

# Exercise 3: String Module
import string
import random

new_string = ''.join(random.choice(string.ascii_letters) for _ in range(5))

## OR

new_string2 = ''
for i in range(5):
    new_string2 += random.choice(string.ascii_letters)

print(new_string)
print(new_string2)

# Exercise 4: Current Date
import datetime

def current_date():
    today = datetime.date.today()
    print(today)

# Exercise 5: Amount of Time Left to Jan 1st

current_date_time = datetime.datetime.now()
jan_1st = datetime.datetime(2026,1,1)

time_to_jan = jan_1st - current_date_time
print(time_to_jan)

# Exercise 6: Birthday and Minutes

birthdate = '1994-10-8 00:00:00'

def minutes_alive(date):
    dob = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.now()

    time_alive = now - dob
    total_mins = round(time_alive.total_seconds() / 60, 2)

    return f"You have been alive for approximately {total_mins} minutes."

print(minutes_alive(birthdate))

# Exercise 7: Faker Module
from faker import Faker
fake = Faker()

user_list = []

def add_users(num):
    for user in range(num):
        user = {
                'name': fake.name(),
                'address': fake.address(),
                'language_code': fake.language_code()
                 }
        user_list.append(user)

add_users(10)
print(user_list)