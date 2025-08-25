-- ExercisesXPGold
-- Exercise 1: DVD Rental
-- 1. Get a list of all rentals which are out (have not been returned.
SELECT * FROM rental
WHERE return_date IS NULL
ORDER BY rental_id;

-- 2. Get a list of all customers who have not returned their rentals.
SELECT 
    c.first_name, 
    c.last_name, 
    COUNT(*) AS unreturned_rentals
FROM rental AS r
JOIN customer AS c ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL
GROUP BY c.first_name, c.last_name
ORDER BY unreturned_rentals DESC;

-- 3. Get a list of all the Action films with Joe Swank.
DROP VIEW IF EXISTS actor_category_film_names;
CREATE VIEW actor_category_film_names AS
SELECT 
	f.title AS movie_title, 
	a.first_name|| ' ' || a.last_name AS actor_name, 
	c.name AS category
FROM film AS f
JOIN film_actor AS fa ON f.film_id = fa.film_id
JOIN actor AS a ON fa.actor_id = a.actor_id
JOIN film_category AS fc ON f.film_id = fc.film_id
JOIN category AS c ON fc.category_id = c.category_id;

SELECT * 
FROM actor_category_film_names
WHERE actor_name = 'Joe Swank' AND category = 'Action';

-- Exercise 2: Happy Halloween - Prepare tables with the following data:
-- 1. How many stores there are, and in which city and country they are located
CREATE VIEW store_city_country_names AS
SELECT ci.city, co.country, count(*) AS store_count
FROM city AS ci
JOIN country AS co ON ci.country_id = co.country_id
JOIN address as a ON ci.city_id = a.city_id
JOIN store AS s ON a.address_id = s.address_id
GROUP BY ci.city, co.country;

-- 2. How many hours of viewing time there are in total in each store
-- 3. Make sure to exclude any inventory items which are not yet returned.
SELECT 
	i.store_id, 
	SUM(f.length) AS viewing_time_minutes
FROM inventory AS i
JOIN film AS f ON i.film_id = f.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL
GROUP BY i.store_id;

-- 4. A list of all customers in the cities where the stores are located.
SELECT c.first_name, c.last_name, ci.city
FROM store AS s
JOIN customer AS c on s.store_id = c.store_id
JOIN address AS a ON s.address_id = a.address_id
JOIN city AS ci on a.city_id = ci.city_id
WHERE ci.city_id IN (
	SELECT a.city_id
	FROM store AS s
	JOIN address AS a ON s.address_id = a.address_id
);

-- 5. A list of all customers in the countries where the stores are located.
SELECT c.first_name, c.last_name, co.country
FROM store AS s
JOIN customer AS c ON s.store_id = c.store_id
JOIN address AS a ON s.address_id = a.address_id
JOIN city AS ci ON a.city_id = ci.city_id
JOIN country AS co ON ci.country_id = co.country_id
WHERE ci.country_id IN (
	SELECT co.country_id
	FROM store AS s
	JOIN address AS a ON s.address_id = a.address_id
	JOIN city AS ci ON a.city_id = ci.city_id
	JOIN country AS co ON ci.country_id = co.country_id
);