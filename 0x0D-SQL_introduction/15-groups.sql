-- Script that list all the numbers of the record with the same score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
