-- Define an index on the first letter of the
-- values in a particular field and the whole
-- values in another field.
CREATE INDEX idx_name_first_score
ON names(name(1), score);
