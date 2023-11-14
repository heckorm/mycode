import requests
import random
import time

API_KEY = 'INSERT_API_KEY'

def get_genre_list():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if 'genres' in data:
        return {genre['id']: genre['name'] for genre in data['genres']}
    else:
        print("Failed to fetch genre list.")
        return {}

def choose_option(genres):
    print("Sit back and relax, let's find you a movie to watch!")
    print("Genres available:")
    for genre_id, genre_name in genres.items():
        print(f"{genre_id}: {genre_name}")
    print("0. Get a random movie")
    choice = input("Enter your choice (genre ID or 0 for random): ")
    return choice

def fetch_movie_by_genre(genre_id):
    if genre_id == '0':
        # Use current timestamp as a seed for random page number
        #random_seed = int(time.time())
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&page=4"
    else:
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"

    response = requests.get(url)
    data = response.json()

    if 'results' in data and len(data['results']) > 0:
        first_movie = data['results'][0]
        print(f"Check this out: {first_movie['title']} ({first_movie['release_date'][:4]})")
        show_movie_details(first_movie['id'])
    else:
        print("Uh oh! We couldn't find a movie for you.")

def show_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if 'title' in data:
        print(f"Overview: {data['overview']}")
        print(f"Average Rating: {data['vote_average']}")
        print(f"Release Date: {data['release_date']}")
        # You can display more details as needed
    else:
        print("We couldn't find the details on this movie.")

genres = get_genre_list()
if genres:
    user_choice = choose_option(genres)
    fetch_movie_by_genre(user_choice)
else:
    print("No genres available.")

