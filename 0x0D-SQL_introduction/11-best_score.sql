-- Lists all records with a score >= 10 of the table second_table from the database in MySQL server
SELECT score, name FROM second_table WHERE score>=10 ORDER BY score DESC;
