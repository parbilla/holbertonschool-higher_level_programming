-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN
(SELECT ts.id
FROM tv_shows ts
JOIN tv_show_genres sg
ON ts.id=sg.show_id
JOIN tv_genres tg
ON tg.id=sg.genre_id
WHERE tg.name='Comedy')
ORDER BY ts.title;
