import pandas as pd

# Load the data from the Excel file
df = pd.read_excel(r"C:\Users\Admin\Documents\excel project files\most_voted__movies_and_series_imdb.xlsx")

# Split the genre column by comma
df_genres = df["Genres"].str.split(",", expand=True)

# Get the number of columns in the split dataframe
num_columns = df_genres.shape[1]

# Generate a list of genre names based on the number of columns
genre_names = []
for i in range(num_columns):
    genre_names.append("Genre" + str(i + 1))

# Set the column names in the split dataframe
df_genres.columns = genre_names

# Concatenate the split dataframe with the original dataframe
df = pd.concat([df, df_genres], axis=1)


# Drop the original 'Genres' column
df = df.drop(["Genres"], axis=1)

# Write the updated dataframe back to the Excel file
df.to_excel(r"C:\Users\Admin\Documents\excel project files\most_voted__movies_and_series_imdb.xlsx", index=False)