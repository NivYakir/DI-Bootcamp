from menu_editor import MenuManager, MenuItem, MenuEditor, cur
import psycopg2

def main():
    
    print("Welcome to the Menu Editor")
    while True:
        me = MenuEditor()
        me.show_user_menu()
        user_input = input("Select one of the above options: ")
        user_input = user_input.upper()

        if user_input not in ['V', 'A', 'D', 'U', 'S']:
            print("Invalid Input.")
        
        if user_input == 'V':
            me.view_item()
        elif user_input == 'A':
            me.add_item_to_menu()
        elif user_input == 'D':
            me.remove_item_from_menu()
        elif user_input == 'U':
            me.update_item_from_menu()
        else:
            me.show_restaurant_menu()
            break
    
main()