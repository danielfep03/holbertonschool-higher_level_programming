-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- Create a new database and a new user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'127.0.0.1' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
