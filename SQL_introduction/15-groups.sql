-- Lists number of records per score, sorted by count DESC
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
