import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class MenuManager:
    def __init__(self):
        with open(f"{dir_path}/restaurant_menu.json", 'r', encoding='utf-8') as file:
            self.menu = json.load(file)
    
    def add_item(self, name, price):
        item = {
            'name' : name,
            'price' : price
        }

        self.menu['items'].append(item)

    def remove_item(self, name):
        for i in range(len(self.menu['items']) - 1, -1, -1):
            if self.menu['items'][i]['name'] == name:
                del self.menu['items'][i]
                return True
        return False

    def save_to_file(self):
        with open(f"{dir_path}/restaurant_menu.json", 'w') as file:
            json.dump(self.menu, file, indent=3)

m1 = MenuManager()

# print(m1.menu)
# m1.add_item("Cheese", 20)
# print(m1.menu)
# m1.remove_item("Milkshake")
# print(m1.menu)
# m1.save_to_file()
