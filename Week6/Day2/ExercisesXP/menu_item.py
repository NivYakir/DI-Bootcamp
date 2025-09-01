import psycopg2, requests, os, json

connection = psycopg2.connect(
    database = 'restaurant',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)

cur = connection.cursor()

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)"
        cur.execute(query, (self.name, self.price))

        connection.commit()
        print(f"'{self.name}' added to menu.")
    
    def delete(self):
        query = "DELETE FROM menu_items WHERE (item_name = %s)"
        cur.execute(query, (self.name,))

        connection.commit()
        print(f"'{self.name}' deleted from menu.")
    
    def update(self, new_name=None, new_price=None):
        """Update the name and/or price of this item.
        Returns True if a row was updated, False otherwise."""
        if not new_name and not new_price:
            raise ValueError("Please enter a new name and/or price")

        if new_price is not None and not isinstance(new_price, (int, float)):
            raise TypeError("Price must be an int or float")

        old_name, old_price = self.name, self.price

        # Update in-memory values
        if new_name:
            self.name = new_name
        if new_price:
            self.price = new_price

        query = """
            UPDATE menu_items
            SET item_name = %s, item_price = %s
            WHERE item_name = %s AND item_price = %s
            RETURNING item_name, item_price
        """
        cur.execute(query, (self.name, self.price, old_name, old_price))
        updated = cur.fetchone()
        connection.commit()

        if updated:
            self.name, self.price = updated
            return True
        return False
    
    def __str__(self):
        return f"'{self.name}' : ${self.price}"