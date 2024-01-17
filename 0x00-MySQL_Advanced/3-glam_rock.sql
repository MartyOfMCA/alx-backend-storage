-- Retrieves the total number of years bands
-- fancying the Glam rock style have lasted.
-- Bands that have split are considered as
-- closed.
SELECT band_name,
	COALESCE(split, 2022) - formed lifespan
FROM metal_bands
WHERE BINARY style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
