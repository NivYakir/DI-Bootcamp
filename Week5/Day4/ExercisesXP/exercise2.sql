-- Exercise 2: DvD Rental Database
-- Select all the columns from the 'customer' table
SELECT * FROM customer

-- Display first_name and last_name as an alias called full_name
SELECT first_name || ' ' || last_name AS full_name
FROM customer

-- Write a query to select all the create_date from customer
SELECT DISTINCT create_date FROM customer

-- Fetch all the customer details, display in descending order by first name
SELECT *
FROM customer
ORDER BY first_name DESC

-- Fetch film id, title, description, year of release and rental rate in ascending order by rate
SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC

-- Fetch address, and phone number of all customers living in the Texas district
SELECT address, phone
FROM address
WHERE district = 'Texas'

-- Write query to retrieve all movie details where the movie ID is 15 or 150
SELECT * FROM film
WHERE film_id IN (15, 150)

-- Write a query which should check if your favorite movie exists in the database. 
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Star Wars'

-- Write a query of all movies that start with the first 2 letters of your favorite movie
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'St%'

-- Write a query that will retriece the 10 cheapest movies
SELECT *
FROM film
ORDER BY rental_rate ASC
LIMIT 10

-- Write a query to find the next 10 cheapest movies
SELECT *
FROM film
ORDER BY rental_rate ASC
OFFSET 10
LIMIT 10

-- Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, 
-- as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer AS c
INNER JOIN payment AS p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC

-- Write a query to get all the movies which are not in inventory
SELECT f.*
FROM film AS f
LEFT JOIN inventory AS i
ON f.film_id = i.film_id
WHERE i.film_id is NULL

-- OR:
SELECT * FROM film
WHERE film_id NOT IN (
	SELECT film_id
	FROM inventory
)

-- Write a query to find which city is in which country.
SELECT ci.city, co.country
FROM country AS co
INNER JOIN city AS ci
ON co.country_id = ci.country_id

-- Bonus: You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount 
-- and the date of payment ordered by the id of the staff member who sold them the dvd.
SELECT
	c.customer_id,
	c.first_name || ' ' || c.last_name AS full_name,
	p.amount,
	p.payment_date,
	p.staff_id
FROM customer AS c
INNER JOIN payment AS p
ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC