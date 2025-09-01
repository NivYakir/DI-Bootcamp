from menu_manager import MenuManager
from menu_item import MenuItem, cur

class MenuEditor:
    def show_user_menu(self):
        print("(V)iew an item\n(A)dd an item\n(D)elete an item\n(U)pdate an item\n(S)how Menu")
    
    def view_item(self):
        item_name = input("Which item would you like to view? ")
        item = MenuManager.get_by_name(item_name)

        if item:
            print(item)
        else:
            print(f"'{item_name}' does not exist in menu.")
    
    def add_item_to_menu(self):
        item_name = input("Enter the item's name: ")
        item_price = input("Enter the item's price: ")

        item = MenuItem(item_name, item_price)
        item.save()
    
    def remove_item_from_menu(self):
        item_name = input("Which item would you like to remove from the menu? ")
        item = MenuManager.get_by_name(item_name)
        
        if item:
            item.delete()
        else:
            print("This item does not exist")

    def update_item_from_menu(self):
        item_name = input("Which item would you like to update? ")
        item = MenuManager.get_by_name(item_name)

        if item:
            name = input("Enter the item's updated name: ")
            price = int(input("Enter the item's updated price: "))
            item.update(name, price)
            print("Item has been successfully updated")
        else:
            print("Error. Item does not exist in the menu.")

    def show_restaurant_menu(self):
        cur.execute('SELECT * FROM menu_items')
        rows = cur.fetchall()
        print('----------MENU----------')
        for i, row in enumerate(rows):
            item_id, item_name, item_price = row
            item_id = i + 1
            print(f"{item_id}: {item_name} - ${item_price}")
