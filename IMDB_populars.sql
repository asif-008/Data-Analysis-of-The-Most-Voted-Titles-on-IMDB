--Chceking if this pair (name, number of votes) can be unique key

SELECT title,[Number of Votes],COUNT([Number of Votes])
FROM imdb_populars.dbo.Sheet1$
GROUP BY title,[Number of Votes]
HAVING COUNT([Number of Votes]) = 1

-- the answer is yes.


--getting the genres in separate columns for a separate spreadsheet.

WITH movie_genres (title, votes, genre1, genre2, genre3) AS (
  SELECT title, [Number of Votes], genre1, genre2, genre3
  FROM imdb_populars.dbo.Sheet1$
)
SELECT title, votes, genre1 AS genre
FROM movie_genres
WHERE genre1 <> '-'
UNION ALL
SELECT title, votes, genre2
FROM movie_genres
WHERE genre2 <> '-'
UNION ALL
SELECT title, votes, genre3
FROM movie_genres
WHERE genre3 <> '-';