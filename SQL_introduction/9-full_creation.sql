-- a script that creates a table called second_table in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO first_table (id, name, score)
VALUES ('1', '2', '3', '4', 'John', 'Alex', 'Bob', 'George', '10', '3', '14', '8');
