# Functions and Data Structures

students = ['Harry', 'Ron', 'Hermione']

# create a function that says 'Name, welcome to Hogwarts! for each name in the list'

def welcome():
    for name in students:
        print(f"Hello {name}, welcome to Hogwarts!")

welcome()

def get_house():
    for i, name in enumerate(students):
        students[i] = f"{name} : Gryffindor"

get_house()
print(students)
