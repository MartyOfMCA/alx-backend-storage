-- Define a view retrieving all students
-- whose score meets a certain threshold.
DELIMITER $$

CREATE VIEW need_meeting
AS
	SELECT name
	FROM students
	WHERE score < 80 AND
	(last_meeting IS NULL OR ADDDATE(last_meeting, INTERVAL 1 MONTH) < CURDATE());
$$

DELIMITER ;
