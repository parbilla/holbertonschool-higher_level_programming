-- Lists all shows from the database hbtn_0d_tvshows_rate by their rating

SELECT ts.title, sum(tr.rate)
FROM tv_shows ts
INNER JOIN tv_show_ratings tr
ON ts.id=tr.show_id
GROUP BY ts.title
ORDER BY sum(tr.rate) DESC;
