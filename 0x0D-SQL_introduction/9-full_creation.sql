-- Create a new table
CREATE TABLE IF NOT EXISTS second_table(
	`id` INTEGER,
	`name` VARCHAR(256),
	`score` INTEGER
);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, 'Jhon', 10);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (2, 'Alex', 3);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (3, 'Bob', 14);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (4, 'George', 8);
