-- Lists all records with non-empty name, sorted by score DESC
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
