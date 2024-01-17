-- Create a new table named users. The new table
-- has a primary key constraint and a unique
-- constraint on the email field. couuntry
-- field is an enumeration of countries.
CREATE TABLE IF NOT EXISTS users
(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country CHAR(2) NOT NULL DEFAULT 'US',
	CHECK (country = 'US' OR country = 'CO' OR country = 'TN')
);
