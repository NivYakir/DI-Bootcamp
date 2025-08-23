-- Exercise 1: Items and Customers

-- All items ordered by price (asc):
SELECT *
FROM ITEMS
ORDER BY price ASC

-- Items with a price above 80 (inclusive), ordered by price (desc):
SELECT * FROM items
WHERE price >= 80
ORDER BY price DESC

-- First 3 customers in alphabetical order, exclude PK column:
SELECT first_name, last_name FROM customers
ORDER BY first_name ASC
LIMIT 3

-- All last names in reverse alphabetical order:
SELECT last_name FROM customers
ORDER BY last_name DESC