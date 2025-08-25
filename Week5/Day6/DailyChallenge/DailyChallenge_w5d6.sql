-- DailyChallenge: Week5 Day6
-- Part 1: 
-- 1. Create 2 tables : Customer and Customer profile. They have a One to One relationship.
CREATE TABLE Customer(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(150) NOT NULL
);

DROP TABLE IF EXISTS CustomerProfile;
CREATE TABLE CustomerProfile(
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT FALSE,
	customer_id INT UNIQUE,
	FOREIGN KEY(customer_id) REFERENCES Customer(id) ON DELETE CASCADE
);

-- 2. Insert below customers.
INSERT INTO Customer(first_name, last_name) VALUES
('John', 'Doe'), 
('Jerome', 'Lalu'), 
('Lea', 'Rive');

-- 3. Insert Customer Profiles using Subqueries.
INSERT INTO CustomerProfile (isLoggedIn, customer_id) VALUES 
	(TRUE, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')),
    (FALSE, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- 4. Use relevant types of JOINS to display:
-- The first_name of the LoggedIn customers
SELECT c.first_name
FROM Customer AS c
INNER JOIN CustomerProfile AS cp
ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT
	c.first_name,
	cp.isLoggedIn
FROM Customer AS c
LEFT JOIN CustomerProfile AS cp
ON c.id = cp.customer_id;

-- The number of customers that are not LoggedIn
SELECT COUNT(*) AS not_logged_in
FROM Customer AS c
INNER JOIN CustomerProfile AS cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = FALSE;

-- Part 2: 
-- 1. Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
DROP TABLE IF EXISTS Book;
CREATE TABLE Book(
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(200) NOT NULL,
	author VARCHAR(200) NOT NULL
);

-- 2. Insert the below books.
INSERT INTO Book(title, author) VALUES
	('Alice in Wonderland', 'Lewis Carroll'),
	('Harry Potter', 'J.K. Rowling'),
	('To Kill a Mockingbird', 'Harper Lee');

-- 3. Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. (Age can't be larger than 15)
DROP TABLE IF EXISTS Student;
CREATE TABLE Student(
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(200) NOT NULL UNIQUE,
	age INTEGER CHECK (age <= 15)
);

-- 4. Insert students:
INSERT INTO Student(name, age) VALUES
	('John', 12), 
	('Lera', 11),
	('Patrick', 10),
	('Bob', 14);

-- 5. Create a Table named Library, with the columns:
DROP TABLE IF EXISTS Library;
CREATE TABLE Library(
	book_fk_id INT,
	student_fk_id INT,
	borrowed_date DATE,
	PRIMARY KEY(book_fk_id, student_fk_id),
	FOREIGN KEY(book_fk_id) REFERENCES Book(book_id) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE,
	FOREIGN KEY(student_fk_id) REFERENCES Student(student_id)
		ON DELETE CASCADE 
		ON UPDATE CASCADE
);

-- 6. Add 4 records in the junction table, use subqueries.
INSERT INTO Library(book_fk_id, student_fk_id, borrowed_date) VALUES
	((SELECT book_id FROM Book WHERE title = 'Alice in Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
	((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
	((SELECT book_id FROM Book WHERE title = 'Alice in Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
	((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');

-- 7. Display the data:
-- Select all the columns from the junction table
SELECT * FROM library;

-- Select the name of the student and the title of the borrowed books
SELECT s.name, b.title
FROM Library AS l
RIGHT JOIN student AS s
	ON l.student_fk_id = s.student_id
RIGHT JOIN book AS b
	ON l.book_fk_id = b.book_id;

-- Select the average age of the children, that borrowed the book Alice in Wonderland
SELECT ROUND(AVG(s.age), 2) AS average_age
FROM Library AS l
RIGHT JOIN student AS s
	ON l.student_fk_id = s.student_id
RIGHT JOIN book AS b
	ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice in Wonderland'
GROUP BY b.title;

-- Delete a student from the Student table, what happened in the junction table?
-- Lera's entry will automatically be deleted from Library, due to the ON DELETE CASCADE restraint placed on the foreign key when the table was created.
DELETE FROM student WHERE name = 'Lera';


