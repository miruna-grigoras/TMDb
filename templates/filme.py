from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_movie_details(movie_title="Inception"):
    API_KEY = os.getenv("API_KEY")
    BASE_URL = "https://api.themoviedb.org/3"
    endpoint = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": movie_title
    }
    
    response = requests.get(endpoint, params=params)
    response_data = response.json()
    
    return response_data

if __name__ == "__main__":
    print('\n*** Get Movie Details ***\n')

    movie_title = input("Please enter a movie title: ")
    
    movie_data = get_movie_details(movie_title)

    print("\n")
    
    # Extrage și afișează doar filmele găsite
    results = movie_data.get("results", [])
    
    if results:
        for movie in results:
            title = movie.get("title", "N/A")
            release_date = movie.get("release_date", "N/A")
            overview = movie.get("overview", "N/A")
            vote_average = movie.get("vote_average", "N/A")
            
            print(f"Title: {title}")
            print(f"Release Date: {release_date}")
            print(f"Overview: {overview}")
            print(f"Vote Average: {vote_average}")
            print("-" * 40)
    else:
        print("No results found for the provided movie title.")
