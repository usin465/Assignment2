import os
from flask import Flask, request, render_template
import webapp.adapters.repository as repo
from webapp.adapters.memory_repository import MemoryRepository
from tests import unit
from markupsafe import escape


def create_app(test_config = None):

    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    if test_config is None:
        app.config.from_object('config.Config')
        data_path = 'webapp/adapters/data/Data1000Movies.csv'

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']
    repo = MemoryRepository()
    repo.populate_repo(data_path)



    @app.route('/')
    def home():
        html_page = render_template('home.html')
        return html_page

    @app.route('/browse_movies')
    def browse_movies():
        list_of_movies = repo.get_first_movies()
        return render_template('movies.html', movies = list_of_movies)

    @app.route('/browse_movies/last')
    def last_movies():
        last_movies = repo.get_last_movies()
        return render_template('movies.html', movies = last_movies)

    @app.route('/browse_movies/first')
    def first_movies():
        first_movies = repo.get_first_movies()
        return render_template('movies.html',movies = first_movies)

    @app.route('/browse_movies/next')
    def next_movies():
        next = repo.get_next_movies()
        return render_template('movies.html', movies = next)

    @app.route('/browse_movies/previous')
    def previous_movies():
        prev = repo.get_previous_movies()
        return render_template('movies.html', movies = prev)




    return app