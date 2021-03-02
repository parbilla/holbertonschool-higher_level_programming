-- Lists the number of records with the same score in the table second_table from the database in MySQL server
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score DESC;
