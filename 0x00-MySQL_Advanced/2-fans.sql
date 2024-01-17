-- Retrieve results for the various origins
-- and the total fans. Results appears in
-- a ranked manner where the origin with
-- the most fans is considered the first.
SELECT origin,
	sum(fans) nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
