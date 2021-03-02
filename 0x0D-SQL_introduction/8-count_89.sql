-- Script that displays the number of records with id = 89 in a table
SELECT id, count(*) FROM first_table
GROUP BY id;
