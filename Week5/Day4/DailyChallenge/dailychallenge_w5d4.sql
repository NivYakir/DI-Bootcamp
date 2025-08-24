-- -- DailyChallenge: 
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)


-- Q1. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL)

-- The output should be 0. The subquery will return a NULL value, thus the result of the 
-- WHERE check in the main query will return an 'unknown' value (NOT a True or False). Since WHERE only keeps rows where the condition is TRUE, 
-- you end up with zero rows, and the count will be 0.

-- Q2. What is the output of the below statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab)

-- Similar to the first Questions, For each ft.id, SQL checks if it’s not equal to all values in that set.
-- But one of the values is NULL. Because of that, the whole NOT IN condition turns into UNKNOWN for every row, 
-- and WHERE results in zero rows matching the condition, so the output is 0.

-- Q3. What is the output:
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- Similar to the first Questions, For each ft.id, SQL checks if it’s not equal to all values in that set.
-- But one of the values is NULL. Because of that, the whole NOT IN condition turns into UNKNOWN for every row, 
-- and WHERE results in zero rows matching the condition, so the output is 0.

-- Q4. What is the output:
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- The subquery result is 5, since that is the only value in SecondTab that isn't NULL. Thus, the query asks to count
-- the number of rows where the FirstTab value isn't equal to 5. There are 2 rows that match this condition, thus
-- the output will be 2.

 