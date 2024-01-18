-- Define a stored procedure that adds a
-- new correction for a stuident. New
-- projects are recorded into the projects
-- table if they don't exist already before
-- the correction is stored.
DELIMITER $$

CREATE PROCEDURE AddBonus
(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
	DECLARE p_id INT DEFAULT -1;

	-- Fetch id for a project if it exists
	SELECT id into p_id
	FROM projects
	WHERE name = project_name;

	IF p_id = -1 THEN
		-- Record new project
		INSERT INTO projects(name)
		VALUES(project_name);

		-- Retrieve id for newly added project
		SELECT id INTO p_id
		FROM projects
		WHERE name = project_name;
	END IF;

	INSERT INTO corrections(user_id, project_id, score)
	VALUES(user_id, p_id, score);
END;
$$

DELIMITER ;
