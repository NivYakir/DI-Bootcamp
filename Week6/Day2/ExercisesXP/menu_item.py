import psycopg2

connection = psycopg2.connect(
    database = 'restaurant',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)

cursor = connection.cursor()

# Exercise 1: Restaurant Menu Manager
# Part 1:
# 1. Create a table called menu_items:

cursor.execute('DROP TABLE IF EXISTS menu_items')
cursor.execute('''CREATE TABLE menu_items(
               item_id SERIAL PRIMARY KEY,
               item_name VARCHAR(30) NOT NULL,
               item_price SMALLINT DEFAULT 0
               )''')

connection.commit()
print('Connection Successful. Table was created.')

# 2. Create a new class called MenuItem, attributes are name and price of an item
# 3. Add save/delete/update methods to the MenuItem class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        '''Add this item into the menu_items table'''
        cursor.execute(f'''INSERT INTO menu_items(item_name, item_price)
                        VALUES ('{self.name}', '{self.price}')''')
        connection.commit()

    def delete(self):
        '''Delete this item from the menu_items table'''
        cursor.execute(f"""DELETE FROM menu_items WHERE item_name = '{self.name}'""")
        connection.commit()
        return cursor.rowcount > 0

    def update(self, new_name=None, new_price=None):
        '''Update the name and/or price of this item.
        If you are only changing the price, make sure to specify'''
        original_name = self.name

        if new_name is None and new_price is None:
            raise ValueError("Please enter a new name and/or price")

        if new_name is not None:
            self.name = new_name

        if new_price is not None:
            if not isinstance(new_price, (int)):
                raise TypeError("Price must be an int or float")
            self.price = new_price

        cursor.execute(f"""UPDATE menu_items
                       SET item_name = '{self.name}', item_price = '{self.price}'
                       WHERE item_name = '{original_name}'""")
        connection.commit()
        return cursor.rowcount > 0


pizza = MenuItem('Pizza', 5)
stew = MenuItem('Beef Stew', 15)
cake = MenuItem('Chocolate Cake', 10)
chips = MenuItem('Chips', 3)
melon = MenuItem('Melon', 7)

pizza.save()
stew.save()
cake.save()
chips.save()