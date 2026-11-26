# Exploring genres, ratings and release years across 2,500 IMDb titles

Which genres appear most often among movies and TV series with at least 100,000 IMDb votes? Drama leads this sample, followed by action and comedy. A title can appear in several genres. The vote threshold tells us which titles qualified; the dataset contains no viewing counts.

[![Tableau dashboard showing genre frequency, average ratings for five popular genres, the distribution of title ratings, and the number of titles by release year.](https://public.tableau.com/static/images/Po/Popularmoviesandtvseries/Dashboard1/1.png)](https://public.tableau.com/views/Popularmoviesandtvseries/Dashboard1)

[Open the interactive Tableau dashboard](https://public.tableau.com/views/Popularmoviesandtvseries/Dashboard1) to explore the charts using the genre and category filters.

## Movies and TV series in the sample

| Category in the workbook | Titles | Share of sample | Median IMDb rating |
|---|---:|---:|---:|
| Movie | 2,264 | 90.56% | 7.1 |
| TV series | 236 | 9.44% | 8.4 |

Movies account for roughly nine in ten titles. The smaller TV series group has a median rating **1.3 points higher**. These are title-level medians, with equal weight for each title regardless of its vote count.

## Explore the data

- The [Tableau workbook input](imdb_populars_tableau.xlsx) has two sheets. To reproduce the table above, group **rating and year** by category, count its rows and take the median of **IMDb Rating**. The **genre** sheet contains multiple rows for titles with multiple genres.
- The [source workbook](imdb_populars_main_source.xlsx) includes the collected titles, ratings, vote counts and intermediate cleaning steps. Excel formulas cleaned the year text and separated start and end years. The project uses the title and vote count together to identify each title in this snapshot.
- The [SQL file](IMDB_populars.sql) documents the transformation into title–genre rows. The dashboard explores genre representation, ratings and release years.

## Collection script

The original [Python scraper](moviesandtv.py) targets the IMDb search-result layout used for this snapshot. With requests, Beautiful Soup, pandas and openpyxl installed, run `python moviesandtv.py` to attempt a fresh collection. It writes `imdb_titles.xlsx` in the working directory. Missing rating elements produce blank cells. An HTTP error or a page with no matching listings stops the export. The saved workbooks allow the analysis to be reproduced independently of IMDb's current layout.
