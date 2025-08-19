-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";

-- CREATE DATABASE "Hollywood" 
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;


-- CREATE TABLE actors(
-- 	actor_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(50) NOT NULL,
-- 	age DATE NOT NULL,
-- 	number_oscars SMALLINT NOT NULL
-- )


-- -- SELECT
-- -- col_1,
-- -- col_2,
-- -- col_3

-- -- FROM
-- -- table_name;


-- -- SELECT * FROM actors;

-- -- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- -- VALUES('Matt','Damon','08/10/1970', 5);

-- -- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- -- VALUES('George','Clooney','06/05/1961', 2);

-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Natalie', 'Portman', '02/10/1976', 1);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Keira', 'Knightly', '04/11/1984', 0);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Leonardo', 'DiCaprio', '04/11/1971', 1);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Al', 'Pacino', '06/11/1955', 3);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Woody', 'Harrelson', '04/02/1968', 1);


-- SELECT first_name || ' ' || last_name as full_name 
-- FROM actors

-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  AND 
-- last_name = 'Damon' ;

-- SELECT first_name, last_name, number_oscars FROM actors WHERE first_name = 'Matt'  OR  
-- number_oscars = 2 ;

-- SELECT * FROM actors WHERE last_name LIKE '%mon%';  --Will fetch any string where 'mon' appears

-- SELECT first_name FROM actors WHERE last_name LIKE '%y' --Will fetch any string ending with y

-- SELECT * FROM actors LIMIT 3  --Limits how many values you wish to query
	
-- SELECT * FROM actors WHERE age > '1960-01-01' LIMIT 3 OFFSET 3  --Skips a specified amount of rows before the query starts

-- SELECT
--     column_1,
--     column_2
-- FROM
--     table_name
-- ORDER BY
--     column_1 [ASC | DESC],
--     column_2 [ASC | DESC];


-- Retrieve all actors sorted by alphabetic last name

-- SELECT 
-- 	first_name || ' ' || last_name as full_name,
-- 	age,
-- 	number_oscars
-- FROM
-- 	actors
-- ORDER BY
-- 	last_name ASC

-- Retrieve first 4 actors in table

-- SELECT * FROM actors LIMIT 4

-- First 4 actors ordered in desc order by last name

-- SELECT * FROM actors ORDER BY last_name

-- Actors that have e in their first name

-- SELECT * FROM actors WHERE first_name LIKE '%e%';

-- Actors that have at least 5 oscars

-- SELECT * FROM actors WHERE number_oscars >= 5









