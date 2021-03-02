-- Script that displays the number of records with id = 89 in a table
select id, count(*) from first_table
group by id;
