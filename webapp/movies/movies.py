from flask import Blueprint
from flask import request, render_template, redirect, url_for, session
import webapp.movies.services as services
import webapp.utilities as utilities
import webapp.adapters.repository as repo

movie_blueprint = Blueprint('movie_bp', __name__)
@movie_blueprint.route('/movies_by_year', methods = ['GET'])
def movies_by_year():
    target_year = request.args.get('year')
    movies = services.get_movies_by_year(target_year,repo)
