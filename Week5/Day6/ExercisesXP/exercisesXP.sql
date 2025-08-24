-- Exercise 1: DVD Rental
-- 1. Get a list of all the languages, from the language table.
SELECT name FROM language;

-- 2. Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT 
	f.title, 
	f.description, 
	l.name AS language
FROM film AS f
INNER JOIN language as l
ON f.language_id = l.language_id;

-- 3. Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT 
    f.title,
    f.description,
    l.name AS language_name
FROM language l
LEFT JOIN film f 
    ON f.language_id = l.language_id;

-- 4. Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film(
	film_id SERIAL PRIMARY KEY,
	name VARCHAR(150)
);

INSERT INTO new_film(name)
VALUES
	('The Departed'),
	('Star Wards'),
	('Saving Private Ryan'),
	('The Prestige'),
	('Spiderman'),
	('The Goodfellas');

-- 5. Create a new table called customer_review
DROP TABLE IF EXISTS customer_review;
CREATE TABLE customer_review(
	review_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL,
    language_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	CONSTRAINT fk_film FOREIGN KEY(film_id) REFERENCES new_film(film_id) ON DELETE CASCADE,
	CONSTRAINT fk_language FOREIGN KEY(language_id) REFERENCES language(language_id)
);

-- 6. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review(film_id, language_id, title, score, review_text) VALUES
(1, 1, (SELECT name FROM new_film WHERE film_id = 1), 10, 'Cinematic Perfection! Best movie I have ever seen in my life!'),
(2, 1, (SELECT name FROM new_film WHERE film_id = 2), 1, 'Absolute trash. Worst movie I have ever seen in my life!');

-- 7. Delete a film that has a review from the new_film table, what happens to the customer_review table?
-- ANSWER: The review will automatically be deleted as well due to the foreign key ON DELETE CASCADE restraint we placed on the customer_review table.
-- QUERY FOR DELETION:
DELETE FROM new_film
WHERE film_id = 2;

-- Exercise 2: DVD Rental
-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 5
WHERE film_id IN (1, 10, 20, 30);

-- 2. Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- ANSWER: address_id and store_id are foreign keys in the customer table. This means that only 'valid' address_id's  or store_id's are allowed to be inserted into this field.
-- By valid, I mean an address_id/store_id that exists within the address/store Tables, otherwise the insert will fail due to the fkey constraint.

-- 3. We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- ANSWER: Yes, this should be easy to do without any additional steps since no field in the customer_review table is a foreign key for another table.
DROP TABLE IF EXISTS customer_review;

-- 4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- ANSWER: 183
SELECT count(*) 
FROM rental 
WHERE return_date IS NULL;

-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT 
	f.title
FROM rental AS r 
JOIN inventory AS i ON r.inventory_id = i.inventory_id
JOIN film AS f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

-- 6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
--    but he can’t remember their names. Can you help him find which movies he wants to rent?

-- a. The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- ANSWER: 'Park Citizen'
SELECT
	f.title,
	f.description,
	a.first_name || ' ' || a.last_name AS actor_name
FROM film AS f
JOIN film_actor AS fa ON f.film_id = fa.film_id
JOIN actor AS a ON fa.actor_id = a.actor_id
WHERE (a.first_name = 'Penelope' AND a.last_name = 'Monroe') AND f.description ILIKE '%sumo%';

-- b. The 2nd film : A short documentary (less than 1 hour long), rated “R”.
-- ANSWER: 'Cupboard Sinners'
SELECT
	f.title,
	f.rating,
	c.name,
	f.length
FROM film AS f
JOIN film_category AS fc ON f.film_id = fc.film_id
JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Documentary' AND f.length < 60 AND f.rating = 'R';

-- -- c. A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
-- -- ANSWER: Sugar Wonka
SELECT
	f.title,
	f.rental_rate,
	r.return_date
FROM film AS f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
JOIN customer AS c ON r.customer_id = c.customer_id
WHERE f.rental_rate > 4 
	AND (r.return_date BETWEEN '28/07/2005' AND '01/08/2005') 
	AND (c.first_name, c.last_name) = ('Matthew', 'Mahan');

-- d. The 4th film : His friend Matthew Mahan watched this film, as well. 
-- 		 It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
-- ANSWER: 'Money Harold'
SELECT
	f.title,
	f.description,
	f.rental_rate
FROM film AS f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
JOIN customer AS c ON r.customer_id = c.customer_id
WHERE (c.first_name, c.last_name) = ('Matthew', 'Mahan')
	AND (f.description ILIKE '%boat%' OR f.title ILIKE '%boat%')
ORDER BY f.rental_rate DESC
LIMIT 1;