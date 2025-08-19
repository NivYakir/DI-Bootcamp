-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	item_type VARCHAR(100) NOT NULL,
-- 	price INT NOT NULL
-- )

-- CREATE TABLE customers (
-- 	customer_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL
-- )


-- 1:
-- INSERT INTO items(item_type, price)
-- VALUES
-- 	('Small Desk', 100),
-- 	('Large Dest', 300),
-- 	('Fan', 80)

-- 2:
-- INSERT INTO customers (first_name, last_name)
-- VALUES
-- 	('Greg', 'Jones'),
-- 	('Sandra', 'Jones'),
-- 	('Scott', 'Scott'),
-- 	('Trevor', 'Green'),
-- 	('Melanie', 'Johnson')

-- 3:
-- a:
SELECT * FROM items

-- b:
SELECT * FROM items WHERE price > 80

-- c:
SELECT * FROM items WHERE price <= 300

-- d:
SELECT * FROM customers WHERE last_name = 'Smith' -- (It will return the table without any results, since there are no customers with the last name 'Smith')

-- e:
SELECT * FROM customers WHERE last_name = 'Jones'

-- f:
SELECT * FROM customers WHERE first_name != 'Scott'






