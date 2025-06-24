-- display groups of people with the same score, labeled with numbers in desc order
SELECT score, COUNT(name) AS number FROM second_table GROUP BY score ORDER BY number DESC;