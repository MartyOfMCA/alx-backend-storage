-- Define a user-defined function that safely
-- devides a numerator by a dividend.
DELIMITER $$

CREATE FUNCTION SafeDiv(first INT, second INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF second = 0 THEN
		RETURN (0);
	ELSE
		RETURN (first / second);
	END IF;
END;
$$

DELIMITER ;
