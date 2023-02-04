import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

# Get the HTML content of the IMDb popular movies page
movies = []


#2499 is determined by manually using the link.
for i in range(1, 2499, 50):
    url = f"https://www.imdb.com/search/title/?num_votes=100000,&sort=num_votes,desc&start={i}&ref_=adv_nxt"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract movie title, year, and IMDb rating from the HTML
    for movie_div in soup.find_all("div", class_="lister-item mode-advanced"):
        title = movie_div.h3.a.text
        year = movie_div.h3.find("span", class_="lister-item-year").text
        num_votes = movie_div.find("span", {"name":"nv"}).get("data-value")
        rating = 0
        genre = movie_div.find("span", class_="genre").text
        try:
            rating = float(movie_div.find("strong").text)
        except AttributeError:
            pass
        movies.append((title, year, rating, genre, num_votes))
    time.sleep(0.1) # delay 0.1 sec between requests




# Create a Pandas dataframe from the extracted data
df = pd.DataFrame(movies, columns=["Title", "Year", "IMDb Rating", "Genres", "Number of Votes"])

# Write the dataframe to an Excel file
df.to_excel(r"C:\Users\Admin\Downloads\ most_voted_thriller_movies_and_series.xlsx", index=False)
