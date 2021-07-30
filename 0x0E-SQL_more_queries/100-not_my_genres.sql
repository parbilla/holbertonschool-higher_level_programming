-- Lists all genres not linked to the show Dexter, from the database hbtn_0d_tvshows

SELECT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN
(SELECT tg.id
FROM tv_genres tg
JOIN tv_show_genres sg
ON tg.id=sg.genre_id
JOIN tv_shows ts
ON ts.id=sg.show_id
WHERE ts.title='Dexter')
ORDER BY tg.name;
