# Exercises XP GOLD
# Part 1: Authentication CLI - login:
import psycopg2
connection = psycopg2.connect(
    database = 'Bootcamp',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)
cursor = connection.cursor()

def create_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS account")
    query = f"""CREATE TABLE {'account'}()"""


# logged_in = None

# while True:
#     user_input = input("Enter 'login' or 'exit': ")
#     if user_input == 'exit':
#         break
    
#     else:
#         username = input("Enter your username: ")
#         if username in my_dict:
#             password = input("Enter your password: ")
#             if my_dict.get(username) == password:
#                 logged_in = username
#                 print ('You have successfully logged in.')
#             else:
#                 print("Incorrect Password.")
#         else:
#             print("Username does not exist. Would you like to create a new account?")
#             while True:
#                 new_user = input('Enter your desired username: ')
#                 if new_user in my_dict:
#                     print("Error: That username already exists! Try again.")
#                 else:
#                     new_pass = input('Enter your desired password: ')
#                     my_dict.update({new_user : new_pass})
#                     print("New account created!")
#                     break

# print(my_dict)