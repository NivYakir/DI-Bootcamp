from menu_manager import MenuManager
import os
import json
dir_path = os.path.dirname(os.path.realpath(__file__))

program_menu ='''
     MENU  
(a) Add an item
(d) Delete an item
(v) View Menu
(x) Exit
          '''

def load_manager():
    menu = MenuManager()
    return menu

def show_user_menu(menu):
    while True:
        print(program_menu)
        user_input = input("Choose one of the above options to proceed: ")
        if user_input == 'a':
            name_input = input("What is the name of the item? ")
            price_input = input("What is the price of this item? ")
            menu.add_item(name_input, price_input)
            print(f"Item {name_input} has been successfully added!")
            continue

        elif user_input == 'd':
            item_input = input("What item do you want to delete? ")
            menu.remove_item(item_input)
            print(f"Item {item_input} has been removed!")
            continue
        
        elif user_input == 'v':
            for item in menu.menu['items']:
                print(f"{item['name']} : {item['price']}")
            continue

        elif user_input == 'x':
            with open(f"{dir_path}/restaurant_menu.json", 'w') as file:
                json.dump(menu.menu, file, indent=3)
            print("You have exited the program.")
            break


menu = load_manager()
show_user_menu(menu)