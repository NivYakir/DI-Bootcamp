# *args and *kwargs
# *args = Arguments = Lists,Tuples,Sets
# **kwargs = Dictionary

students = ['Harry', 'Ron', 'Hermione']

def welcome(*args):     # * = sequence ** = key,word values (dicts)
    print(args)
    if args:
        for name in args:
            print(f"Hello {name}, welcome to Hogwarts!")
    else:
            print("You didn't pass names")

# welcome(students)
welcome('Camila','Niv','Michal','David')

def user_info(**kwargs):
     print(kwargs)
     for value in kwargs.values():
          print(value)

user_info(name = 'Juliana', email = 'juliana@gmail.com', age = 30, is_online = True, pets = ['cat', 'dog'])