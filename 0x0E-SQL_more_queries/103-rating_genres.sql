-- Lists all genres from the database hbtn_0d_tvshows_rate by their rating

SELECT tg.name, sum(tr.rate) AS 'rating'
FROM tv_genres tg
INNER JOIN tv_show_genres sg
ON tg.id=sg.genre_id
JOIN tv_show_ratings tr
ON sg.show_id=tr.show_id
GROUP BY tg.name
ORDER BY sum(tr.rate) DESC;
