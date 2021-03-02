-- Lists all records of the table second_table from the database in MySQL server
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name!='' ORDER BY score DESC;
