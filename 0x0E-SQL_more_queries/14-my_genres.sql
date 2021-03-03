-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tg.name
FROM tv_genres tg
INNER JOIN tv_show_genres sg
ON tg.id=sg.genre_id
JOIN tv_shows ts
ON ts.id=sg.show_id
WHERE ts.title='Dexter'
ORDER BY tg.name;
