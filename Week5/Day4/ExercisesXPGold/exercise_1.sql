-- ExercisesXPGold 
-- Exercise 1: DVD Rental
-- 1: Find out how many films there are for each rating.
SELECT rating, count(*)
FROM film
GROUP BY rating

-- 2: Get a list of all the movies that have a rating of G or PG-13.
SELECT title, rating
FROM film
WHERE rating IN ('G', 'PG-13')

-- Look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
SELECT title, rating, rental_rate, length
FROM film
WHERE length < 120 AND rental_rate < 3 AND rating IN ('G', 'PG-13')
ORDER BY title ASC

-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
UPDATE customer
SET
	first_name = 'Niv',
	last_name = 'Yakir',
	email = 'niv.yakir@sakilacustomer.org'
WHERE customer_id = 2

-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).

SELECT c.first_name, c.last_name, c.address_id, a.address
FROM customer AS c
JOIN address AS a ON c.address_id = a.address_id
WHERE c.customer_id = 2

UPDATE address
SET
	address = '123 Dank Street'
WHERE address_id = 6
