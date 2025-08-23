-- Exercise 3: Items and Customers
-- Part 1: Create purchases table

CREATE TABLE purchases(
	id SERIAL PRIMARY KEY,
	customer_id INT,
	item_id INT,
	quantity_purchased SMALLINT,
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
	FOREIGN KEY(item_id) REFERENCES items(item_id)
)

-- Insert purchases for the customers, use subqueries
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES
	((SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'), 
	(SELECT item_id FROM items WHERE item_name = 'Fan'), 1),
	
	((SELECT customer_id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
	(SELECT item_id FROM items WHERE item_name = 'Large Desk'), 10),
	
	((SELECT customer_id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
	(SELECT item_id FROM items WHERE item_name = 'Small Desk'), 2)

-- Part 2
-- 1: Use SQL to get the following from the Database
-- a. All purchases. Is this information useful to us?
SELECT * FROM purchases -- No, from this table alone we do not get any useful information besides quantity purchased. We do not know the item name or price. We also don't know the customer's information.

-- b. All purchases, joining with the customers table.
SELECT p.*, c.*
FROM purchases AS p
LEFT JOIN customers AS c
ON p.customer_id = c.customer_id

-- c. Purchases of the customer with the ID equal to 5
SELECT
	p.*,
	c.first_name || ' ' || c.last_name as customer_name
FROM purchases AS p
LEFT JOIN customers AS c
ON p.customer_id = c.customer_id
WHERE p.customer_id = 5

-- d. Purchases for a large desk AND a small desk
SELECT
	p.*
FROM purchases AS p
FULL JOIN items AS i
ON p.item_id = i.item_id
WHERE item_name LIKE '%Desk'

-- 2: Use SQL to show all the customers who have made a purchase. Show the following fields/columns: first_name, last_name, item_name
SELECT c.first_name, c.last_name, i.item_name
FROM purchases AS p
INNER JOIN customers AS c
ON p.customer_id = c.customer_id
INNER JOIN items AS i
ON p.item_id = i.item_id

-- 3: Add a row which references a customer by ID, but does not reference an item by ID (leave it blank).
-- Does this work? Why/why not?

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (4, NULL, 10)

-- It only works if you use a NULL value to represent the item_id, since we didn't give a constraint when creating the table that the value must be filled.


