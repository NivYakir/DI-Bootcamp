from datetime import datetime

user_input = input("Please enter your birthdate in DD/MM/YYYY Format: ")
date = user_input.split('/')
my_age = 2025 - int(date[2])

print(f"""
       
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~


""")