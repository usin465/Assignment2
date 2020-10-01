from webapp.adapters.repository import AbstractRepository
from webapp.domain.model import Movie,MovieFileCSVReader

def get_movies_by_year(year, repo = AbstractRepository)
    movies = repo.get_movies_by_year(target_year = year)
