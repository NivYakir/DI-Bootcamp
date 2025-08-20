-- Database: Bootcamp

-- DROP DATABASE IF EXISTS "Bootcamp";

-- CREATE DATABASE "Bootcamp"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE students (
-- 	student_ID SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL,
-- 	birth_date DATE NOT NULL
-- )

-- INSERT INTO students (first_name, last_name, birth_date)
-- VALUES
-- 	('Marc', 'Benichou', '02/11/1998'),
-- 	('Yoan', 'Cohen', '03/12/2010'),
-- 	('Lea', 'Benichou', '27/07/1987'),
-- 	('Amelia', 'Dux', '07/04/1996'),
-- 	('David', 'Grez', '14/06/2003'),
-- 	('Omer', 'Simpson', '03/10/1980'),
-- 	('Niv', 'Yakir', '08/10/1994')

-- -- 1:
-- -- SELECT * FROM students

-- -- 2: 
-- SELECT first_name, last_name
-- FROM students

-- -- 3:
-- a:
-- SELECT first_name, last_name
-- FROM students
-- WHERE student_id = 2

-- -- b:
-- SELECT first_name, last_name
-- FROM students
-- WHERE last_name = 'Benichou' AND first_name = 'Marc'

-- -- c:
-- SELECT first_name, last_name
-- FROM students
-- WHERE last_name = 'Benichou' OR first_name = 'Marc'

-- -- d:
-- SELECT first_name, last_name
-- FROM students
-- WHERE first_name LIKE '%a%'

-- -- e:
-- SELECT first_name, last_name
-- FROM students
-- WHERE first_name ILIKE 'a%'

-- -- f:
-- SELECT first_name, last_name
-- FROM students
-- WHERE first_name ILIKE '%a'

-- -- g:
-- SELECT first_name, last_name
-- FROM students
-- WHERE SUBSTRING(first_name FROM LENGTH(first_name)-1 FOR 1) = 'i'

-- -- h:
-- SELECT first_name, last_name
-- FROM students
-- WHERE student_id = 1 OR student_id = 3

-- -- 4:
-- SELECT * FROM students
-- WHERE birth_date >= '01/01/2000'

-- ExercisesXPGOLD
-- 1:
-- SELECT * FROM students
-- ORDER BY last_name ASC
-- LIMIT 4

-- 2:
-- SELECT * FROM students
-- ORDER BY birth_date DESC
-- LIMIT 1

-- 3:
-- SELECT * FROM students LIMIT 3 OFFSET 2