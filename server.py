import os
from flask import Flask, render_template, request
from waitress import serve
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/movies')
def get_movies():
    movie_name = request.args.get('movie_name')

    if not movie_name:
        return render_template('filme_negasite.html', message="Nu ați furnizat un nume de film")

    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": movie_name
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            movies = data.get("results", [])

            if not movies:
                return render_template('filme_negasite.html', message="Nu am fost găsite rezultate pentru numele filmului furnizat")

            return render_template("movies.html", movies=movies)
        else:
            return render_template('filme_negasite.html', message="Eroare la conectarea cu API-ul TMDb")
    except Exception as e:
        return render_template('filme_negasite.html', message=f"A apărut o eroare: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
