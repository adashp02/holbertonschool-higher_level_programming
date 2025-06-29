-- lists all shows, and all genres linked to that show, if no genre - NULL
SELECT
    t.title,
    g.name
FROM
    tv_shows AS t
LEFT JOIN
    tv_show_genres AS s
ON
    t.id = s.show_id
LEFT JOIN
    tv_genres AS g
ON
    g.id = s.genre_id
ORDER BY
    title ASC,
    name ASC;