-- shows by genre
SELECT tv_genres.name AS genre, count(tv_genres.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;

-- JOIN tv_show_genres ON tv_show_genres.show_id = tv_show_genres.genre_id ORDER BY tv_show_genres.genre_id DESC;
