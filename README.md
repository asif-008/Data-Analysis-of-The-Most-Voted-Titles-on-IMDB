# Data Analysis of The Most Voted Titles on IMDB

## Overview

A data visualization and analysis project on the movies and tv series with more than 100,000 votes on the IMDB website. 

## Data Collection

The data was collected by scraping the website using a Python script. The resulting data format consisted of the following columns: title, year, IMDB rating, number of votes, and genres.

## Data Cleaning

Data of the 'year' column had roman characters, brackets which was cleaned by using excel formulas.

## Data Processing

The data of the 'year' column was broken up into two columns - beginning year and ending year, to separate movie and TV series data. A column named 'category' was added to show if the object is a movie or tv series. The 'genres' column was broken up into separate columns, each containing name of one genre. A separate sheet was created with the data format of (title, vote, genre). The title-vote pair was used as the unique key after verifying that they were all unique. SQL was used to generate the new table.

## Data Preparation

For the visualization, only two table were needed. these two table was copied in a new excel file in different sheets.

## Data Analysis

Tableau was used to create five different visualizations and a dashboard. The following is a description of each visualization:

1. Number of Movies and TV Series: This visualization shows the count of movies and TV series in the data.
2. Genres and their Percentage: This visualization shows the  genres presented in the data and their percentage values.
3. Comparison of Ratings Among Popular Genres: This visualization compares the ratings of the most popular genres in the data.
4. Rating Distribution in Movies and TV series: This visualization shows the distribution of ratings of the most popular titles on the IMDB.
5. Number of Movies Over Time: This visualization helps to identify the years which gave us the most popular movies and tv series.

## Conclusion

This project provides a brief analysis of the most acclaimed movies and TV series. The visualizations and dashboard created in Tableau can be used to explore the data and gain a deeper understanding of people's interest, evolution of movies.
