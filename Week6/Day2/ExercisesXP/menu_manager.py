import psycopg2
from menu_item import MenuItem, cur

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = "SELECT item_name, item_price FROM menu_items WHERE item_name = %s"
        cur.execute(query, (name, ))
        exists = cur.fetchone()

        if exists:
            item_name, item_price = exists
            return MenuItem(item_name, item_price)
        else:
            return None

    @classmethod
    def all_items(cls):
        query = 'SELECT * FROM menu_items'
        cur.execute(query)
        rows = cur.fetchall()

        return [row[1] for row in rows]
