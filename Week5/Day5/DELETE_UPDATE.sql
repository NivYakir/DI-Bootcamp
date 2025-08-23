-- CREATE TABLE colors (
--     color_id SERIAL PRIMARY KEY,
--     name VARCHAR(50)
-- );

--  INSERT INTO colors (name) VALUES ('blue'), ('yellow'), ('pink');
--  SELECT * FROM colors

-- CREATE TABLE cars_restrict (
--     car_id SERIAL PRIMARY KEY,
--     car_name VARCHAR(100),
--     car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT ON UPDATE RESTRICT
-- );

-- INSERT INTO cars_restrict (car_name, car_color) VALUES ('Toyota', 1), ('Ford', 2), ('Honda', 3);


-- DELETE FROM colors WHERE name = 'blue' -- GIVES AN ERROR DUE TO THE ON DELETE RESTRICT syntax
-- ON DELETE OR ON UPDATE CASCADE: it will delete the row and the reference on the child will be deleted as well

-- CREATE TABLE cars_cascade (
--     car_id SERIAL PRIMARY KEY,
--     car_name VARCHAR(100),
--     car_color INTEGER REFERENCES colors (color_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- INSERT INTO cars_cascade (car_name, car_color) VALUES ('Toyota', 1), ('Ford', 2), ('Honda', 3);

-- SELECT * FROM cars_cascade

-- DELETE FROM colors WHERE name = 'blue' -- THIS COMPLETELY DELETES THE ROW OF CAR WHICH WAS ASSOCIATED WITH THE COLOR BLUE

-- UPDATE colors SET color_id = 10 WHERE color_id = 2;


