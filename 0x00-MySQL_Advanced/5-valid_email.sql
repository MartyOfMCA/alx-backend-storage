-- Define a trigger that resets a table
-- field's value when another field changes.
DELIMITER $$

CREATE TRIGGER trgEmailUpdated
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
$$

DELIMITER ;
