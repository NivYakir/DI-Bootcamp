# Exercise 1:

def get_full_name(first, last, middle=None):
    if middle is not None:
        return f"{first.capitalize()} {middle.capitalize()} {last.capitalize()}"
    return f'{first.capitalize()} {last.capitalize()}'

print(get_full_name(first="john", middle="hooker", last="lee"))