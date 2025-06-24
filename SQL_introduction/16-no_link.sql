-- display only score and names only if the name is not a null value in desc order
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;