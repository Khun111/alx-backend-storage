-- SQL script that lists all bands with Glam rock as their main style
SELECT band_name, (2022 - formed) lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
