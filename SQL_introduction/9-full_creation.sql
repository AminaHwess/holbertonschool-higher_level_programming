-- a script that creates a table called second_table in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO first_table (id, name, score)
VALUES  ('1', 'John', '10')
        ('2', 'Alex', '3')
        ('3', 'Bob', '14')  
        ('4', 'George', '8');
