import pandas as pd
import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from requests.exceptions import RequestException


def fetch_omdb_data(title, api_key , retries=3, delay=1):

    # print( "\nf title: " + title)
    # print( "\nf api_key: " + str(api_key))

    """
    Fetch movie data from OMDb API using the title.
    :param title: Title of the movie.
    :param api_key: Your OMDb API Key.
    :return: A dictionary with movie data.
    """
    base_url = "http://www.omdbapi.com/"
    params = {
        't': title,
        'apikey': api_key
    }

    for _ in range(retries):
        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise RequestException("API request failed with status code " + str(response.status_code))
        except RequestException as e:
            print(f"Request failed: {e}, retrying...")
            time.sleep(delay)
    return {}

    # response = requests.get(base_url, params=params)

    # # print(response.url)

    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     return {}

def main():

    file_path = './data.csv'  # Replace with your dataset file path
    df = pd.read_csv(file_path)

    new_columns = [
        'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 
        'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Poster', 'Ratings', 
        'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type', 'totalSeasons', 'Response'
    ]

    for col in new_columns:
        df[col] = None

    api_key = os.environ.get('OMDB_API')  # Replace with your OMDb API key

    # print("\nmovie title original df: " + df['Title'][0])
    # movie = fetch_omdb_data(df['Title'][0], api_key)
    # print("\nResponse " + str(movie))

    # Initialize tqdm progress bar
    pbar = tqdm(total=len(df), desc="Processing", unit="row")

    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
        future_to_index = {executor.submit(fetch_omdb_data, row['Title'], api_key): index for index, row in df.iterrows()}
        
        for future in as_completed(future_to_index):
            index = future_to_index[future]
            try:
                movie_data = future.result()
                if movie_data.get('Response') == 'True':
                    for col in new_columns:
                        df.at[index, col] = movie_data.get(col)
            except Exception as e:
                print(f"Error processing index {index}: {e}")

            pbar.update(1)

    pbar.close()

    # for index, row in df.iterrows():
    #     movie_data = fetch_omdb_data(row['Title'], api_key)
    #     if movie_data.get('Response') == 'True':
    #         for col in new_columns:
    #             df.at[index, col] = movie_data.get(col)

    #     pbar.update(1)

    # # Close the progress bar
    # pbar.close()

    df.to_csv('data_enriched.csv', index=False)

if __name__ == "__main__":
    main()

