-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- List allscript that lists all shows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_shows_genders ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title