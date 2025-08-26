# Exercise 1: Restaurant Menu Manager (cont.)
import psycopg2
connection = psycopg2.connect(
    database = 'restaurant',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)
cursor = connection.cursor()

# 4. Create a new class called MenuManager
class MenuManager:
    @classmethod
    def get_by_name(cls, cursor, name):
        '''Returns a row depending on the item name that is specified'''

        query = 'SELECT * FROM menu_items WHERE item_name = %s'
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        return result

    @classmethod
    def all_items(cls, cursor):
        '''Returns all rows in the menu_items table'''

        query = 'SELECT * FROM menu_items'
        cursor.execute(query)
        rows = cursor.fetchall()

        return [row for row in rows]