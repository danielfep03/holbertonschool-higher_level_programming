-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- Lists data that match a characteristic

SELECT id, name FROM cities WHERE state_id=1 ORDER BY cities.id;
