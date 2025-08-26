# Part 2: 
from menu_manager import MenuManager
from menu_item import MenuItem
import psycopg2
connection = psycopg2.connect(
    database = 'restaurant',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)
cursor = connection.cursor()

# 1. view_item()
def view_item(cursor):
    item_name = input('Which item would like to view?\n')
    item = MenuManager.get_by_name(cursor, item_name)

    if item:
        print(item)
    else:
        print("Error: Item not found in the menu")

# 2. add_item_to_menu()
def add_item_to_menu():
    item_name = input("What is the name of the item?\n")
    price_input = input("What is the item price?\n")
    try:
        price_input = int(price_input)
    except ValueError:
        print("Invalid price. Must be a number.")
        return

    item = MenuItem(item_name, price_input)
    item.save()
    print(f"{item_name} has been added to the menu.")

# 3. remove item from menu function:
def remove_item_from_menu():
    item_name = input("What item would you like to delete?\n")
    item = MenuItem(item_name, 0)

    try:
        success = item.delete()
        if success:
            print(f'{item_name} has been removed from the menu')
        else:
            print(f'Error: could not find {item_name} in the menu')
    except Exception as e:
        print(f'An error has occured: {e}')

# 4. update_item_from_menu()
def update_item_from_menu():
    item_name = input("Which item would you like to update?\n")
    new_name = input("What would like the new name of the item to be?\n")
    new_price = int(input("What would like the new price of the item to be?\n"))

    item = MenuItem(item_name, 0)
    try:
        success = item.update(new_name=new_name, new_price=new_price)
        if success:
            print(f"'{item_name}' successfully updated.\nNew Name: '{new_name}'\nNew Price: {new_price}")
        else:
            print("Error: Something went wrong.")
    except Exception as e:
        print(f'An error has occured: {e}')

# 5. show the restaurant menu:
def show_restaurant_menu(cursor):
    for item in MenuManager.all_items(cursor):
        print(item)


def show_user_menu():
    menu = '(V)iew an item\n(A)dd an item\n(D)elete an item\n(U)pdate an item\n(S)how the menu'
    while True:
        print(menu)
        choice = input(f"Choose an option: ")
        choice = choice.upper()
        if choice not in ['V', 'A', 'D', 'U', 'S']:
            print("Invalid Entry\n")

        elif choice == 'V':
            view_item(cursor)
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        else:
            show_restaurant_menu(cursor)
            break

show_user_menu()