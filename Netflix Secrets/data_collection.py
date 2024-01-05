import pandas as pd
import requests
from datetime import datetime
import json


# Load your Netflix data
file_path = './ex.csv'  # Replace with the path to your Excel file
netflix_data = pd.read_csv(file_path)

# Your TMDb API Key
api_key = '6f625031ac95f1f14b5106c72088295d'

# Define a function to search for a movie and get details
def get_movie_details(title, release_year=None):
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}'
    
    # Make the search request
    search_response = requests.get(search_url)
    if search_response.status_code != 200:
        return None
    
    search_results = search_response.json()['results']
    print(f'\n RY: {title}' )
    print(f' RY: {release_year}\n' )


    print(search_results)
    
    # Find the correct movie (you can enhance this logic)
    for movie in search_results:
        if release_year and 'release_date' in movie and movie['release_date'].startswith(str(release_year)):
            return movie
        elif not release_year:
            return movie

    return None

get_movie_details('Kaleidoscope: Limited Series	', 2022)

'''
# Define the additional columns you want to add
additional_columns = ['Genre', 'Director', 'Cast', 'Runtime', 'User Rating']
for col in additional_columns:
    netflix_data[col] = None

# Iterate over the rows in your dataset
for index, row in netflix_data.iterrows():
    release_date = row.get('Release_Date')
    if pd.notna(release_date):
        release_date = datetime.strptime(release_date, '%Y-%m-%d').strftime('%Y-%m-%d')

    movie_details = get_movie_details(row['Title'], release_date)  # Assuming you have a 'Release Year' column

    print(row['Title'])
    print(movie_details)
    

    # \'''
    if movie_details:
        # Extract the desired information and append it to your dataset
        # Here's an example for genre; you can do similarly for others
        if 'genres' in movie_details and len(movie_details['genres']) > 0:
            netflix_data.at[index, 'Genre'] = movie_details['genres'][0]['name']
        # Add similar code for 'Director', 'Cast', 'Runtime', 'User Rating'
        # \'''

# Save the enriched DataFrame to a new Excel file
netflix_data.to_csv('enriched_netflix_data.csv')
'''