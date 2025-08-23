-- JOINS

-- -- INNER JOINS: See only related rows from both tables
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors 
-- INNER JOIN movies 
-- ON actors.actor_id = movies.actor_playing_id

-- -- LEFT JOIN: See ALL columns belonging to the 'left' table (FROM table)
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- LEFT JOIN movies 
-- ON actors.actor_id = movies.actor_playing_id

-- INSERT INTO movies(movie_title, movie_story, actor_playing_id)
-- VALUES ('The Lord of the Rings - Fellowship of the Ring',
-- 'The Fellowship of the Ring is the first of three volumes in The Lord of the Rings, an epic set in the fictional world of Middle-earth.',
-- NULL)

-- -- RIGHT JOIN: See ALL columns belonging to the 'right' table (JOINED table)
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- RIGHT JOIN movies 
-- ON actors.actor_id = movies.actor_playing_id

-- -- FULL JOIN: Shows all the rows from both tables
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- FULL JOIN movies 
-- ON actors.actor_id = movies.actor_playing_id

-- CREATE TABLE countries(
-- 	country_id SERIAL PRIMARY KEY,
-- 	country_name VARCHAR(50) NOT NULL
-- )

-- INSERT INTO countries(country_name)
-- VALUES
-- 	('Israel'),
-- 	('United States'),
-- 	('Germany'),
-- 	('France'),
-- 	('United Kingdom'),
-- 	('China')

SELECT countries.country_name, actors.first_name, actors.last_name
FROM actors
LEFT JOIN countries
ON actors.actor_id = countries.country_id






