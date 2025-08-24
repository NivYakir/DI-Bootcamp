-- -- DailyChallenge: 
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


-- Q1. What will be the OUTPUT of the following statement?
-- The output should be 0. The subquery will return a NULL value, thus the result of the 
-- WHERE check in the main query will return an 'unknown' value (NOT a True or False). Since WHERE only keeps rows where the condition is TRUE, 
-- you end up with zero rows, and the count will be 0.
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL);

-- Q2.
-- The OUTPUT will be: 0. Similar to the first Questions, For each ft.id, SQL checks if it’s not equal to all values in that set.
-- But one of the values is NULL. Because of that, the whole NOT IN condition turns into UNKNOWN for every row, 
-- and WHERE results in zero rows matching the condition, so the output is 0.
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab);

-- Q3.
-- The OUTPUT for the statement is: 0.
-- If SecondTab.id contains even one NULL, then the entire NOT IN comparison for every row becomes UNKNOWN (never TRUE). 
-- That means no rows match, and the result will be: 0
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab);


-- Q4
-- The subquery result is 5, since that is the only value in SecondTab that isn't NULL. Thus, the query asks to count
-- the number of rows where the FirstTab value isn't equal to 5. There are 2 rows that match this condition, thus
-- the output will be 2.
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL);

 