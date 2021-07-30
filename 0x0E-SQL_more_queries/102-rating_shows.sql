-- Lists all shows from the database hbtn_0d_tvshows_rate by their rating

SELECT ts.title, SUM(tr.rate)
FROM tv_shows ts
JOIN tv_show_ratings tr
ON ts.id=tr.show_id
GROUP BY ts.title
ORDER BY SUM(tr.rate) DESC;
