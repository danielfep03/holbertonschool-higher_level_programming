-- Script that creates the database hbtn_0d_usa and the table cities
-- Creates a new database and a new table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	`id` INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`state_id` INTEGER NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
