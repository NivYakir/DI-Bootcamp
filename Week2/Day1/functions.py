# Functions 

# A reuasble block of code that runs when you 'call' it.

# Syntax:

def func_name():
    '''Prints a string on the console''' # Docstrings: Explain the functionality of a function.
    print("I am a function")

# func_name()  # This is how you call a function.

# Create a function that prints "hello there!", then call the function to see the output.

def hello_func():
    '''Prints the sentence "hello world!"'''
    print("hello there!")

# Passing ARGUMENTS to the function

def greetings(language):
    '''Prints a greeting in the chosen language'''
    if language == 'PT':
        print("Ola, tudo bem?")
    elif language == 'ES':
        print("Hola, que tal?")
    else:
        print("Unknown language")


# greetings() # Will provide an error since you didn't include an Argument

def greetings_ad(language, name):
    '''Prints a greeting to a name in the chosen language'''
    if language == 'PT':
        print(f"Ola {name}, tudo bem?")
    elif language == 'ES':
        print(f"Hola {name}, que tal?")
    else:
        print("Unknown language")


# Key Word Arguments *kwargs

def greetings_adv(name = 'Pedro', language = 'ES'):
    '''Prints a greeting to a name in the chosen language'''
    if language == 'PT':
        print(f"Ola {name}, tudo bem?")
    elif language == 'ES':
        print(f"Hola {name}, que tal?")
    else:
        print("Unknown language")

# greetings_adv('Pedro', 'ES')

# Default values arguments

def greetings_ads(language = 'EN', name = 'John'):
    '''Prints a greeting to a name in the chosen language'''
    if language == 'PT':
        print(f"Ola {name}, tudo bem?")
    elif language == 'ES':
        print(f"Hola {name}, que tal?")
    elif language == 'EN':
        print(f"Hello {name}, how are you?")
    else:
        print("Unknown language")

# greetings_ads()  # notice that I didn't put any arguments when calling
                   # the function, that's becuse default args are the input value.


def calculation(num1, num2) -> int:
    '''returns the sum of 2 numbers'''
    result = num1 + num2
    return result

def multiply(calc) -> int:
    '''takes a number and multiplies by 5'''
    result = calc * 5
    return result

calc = calculation(5, 3)
print(multiply(calc))


def greetings_new(language = 'EN', name = 'John') -> str:
    '''returns a greeting to a name, depending on the chosen language'''
    if language == 'PT':
        return f"Ola {name}, tudo bem?"
    elif language == 'ES':
        return f"Hola {name}, que tal?"
    elif language == 'EN':
        return f"Hello {name}, how are you?"
    else:
        return "Unknown language"
    

# Create a function called country_info that receives a country name as arg
# and prints the capital of that country. Make the country name arg default
# Naboo. It's capital is Theed

def country_info(country_name = 'Naboo') -> str:
    '''Returns the capital of the chosen country'''
    if country_name == f"{country_name}'s capital is Jerusalem":
        return 'Jerusalem'
    elif country_name == 'US':
        return f"{country_name}'s capital is Washington DC"
    elif country_name == 'Argentina':
        return f"{country_name}'s capital is Buenos Aires"
    elif country_name == 'Naboo':
        return f"{country_name}'s capital is Theed"
    else:
        return f'No info available on {country_name}'

print(country_info())

# Global and Local Scope

age = 25   # global variable

def current_age():
    my_age = 30
    my_age += 1

current_age()

def happy_birthday():
    global age
    age += 1
    print(age)

happy_birthday()