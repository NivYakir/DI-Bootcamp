# # *args and *kwargs
# # *args = Arguments = Lists,Tuples,Sets
# # **kwargs = Dictionary

# students = ['Harry', 'Ron', 'Hermione']

# def welcome(*args):     # * = sequence ** = key,word values (dicts)
#     print(args)
#     if args:
#         for name in args:
#             print(f"Hello {name}, welcome to Hogwarts!")
#     else:
#             print("You didn't pass names")

# # welcome(students)
# welcome('Camila','Niv','Michal','David')

# def user_info(**kwargs):
#      print(kwargs)
#      for value in kwargs.values():
#           print(value)

# user_info(name = 'Juliana', email = 'juliana@gmail.com', age = 30, is_online = True, pets = ['cat', 'dog'])

# # my_list = [[1,2],[3,4],[5,6],[7,8],[9,10]]
# # my_listv2 = [[1,2],[3,4],[5,6],[7,8],[9,10]]

# # def show_me(**args):
# #     print(args)

# # show_me(list1=my_list,list_2=my_listv2)
