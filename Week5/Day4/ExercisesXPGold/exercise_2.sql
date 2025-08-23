-- Exercise 2: Students Table
-- ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
UPDATE students
SET birth_date = '02/11/1998'
WHERE last_name = 'Benichou';

-- Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students
SET last_name = 'Guez'
WHERE last_name = 'Grez'

-- Delete the student named 'Lea Benichou' from the table
DELETE FROM students
WHERE student_id = 3

-- Count how many students are in the table
SELECT count(*) FROM students

-- Count how many students were born after 01/01/2000
SELECT COUNT(*)
FROM students
WHERE birth_date > '01/01/2000'

-- Add a column to the table called math_grade
ALTER TABLE students
ADD COLUMN math_grade INT;

-- Add 80 to the student which id is 1.
UPDATE students
SET math_grade = 80
WHERE student_id = 1

-- Add 90 to the students which have ids of 2 or 4.
UPDATE students
SET math_grade = 90
WHERE student_id IN (2,4)

-- Add 40 to the student which id is 6.
UPDATE students
SET math_grade = 40
WHERE student_id = 6

-- Count how many students have a grade bigger than 83
SELECT count(*)
FROM students
WHERE math_grade > 83

-- Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students(first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', '03/10/1980', 70)
RETURNING *
