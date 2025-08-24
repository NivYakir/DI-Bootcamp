-- ExercisesXPNinja Week5 Day4
-- Exercise 1: Bonus Public Database
-- 1: Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT first_name || ' ' || last_name AS customer
FROM customers
ORDER BY customer ASC
OFFSET (SELECT count(*) FROM customers) - 2

-- 2: Use SQL to delete all purchases made by Scott.
DELETE FROM purchases
WHERE customer_id = (SELECT customer_id FROM customers WHERE first_name = 'Scott')

SELECT p.*,
	   c.first_name,
	   c.last_name
FROM purchases as p
INNER JOIN customers as c
ON p.customer_id = c.customer_id

-- 3: Does Scott still exist in the customers table, even though he has been deleted? Try and find him. 
Yes, since we only removed a row from the purchases table, and the customers table is unaffected.
SELECT * FROM customers WHERE first_name = 'Scott'

-- 4: Use SQL to find all purchases...
SELECT 
	p.*,
	c.*
FROM purchases AS p
RIGHT JOIN customers AS c
ON p.customer_id = c.customer_id

-- 5: 
SELECT 
	p.*,
	c.*
FROM purchases AS p
INNER JOIN customers AS c
ON p.customer_id = c.customer_id






