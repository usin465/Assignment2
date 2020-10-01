import csv
import pytest
from webapp.domain.model import MovieFileCSVReader, Movie
from webapp.adapters.memory_repository import MemoryRepository
from tests import unit



@pytest.fixture
def repo():
    filename = 'movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    movie_set = movie_file_reader.dataset_of_movies
    movies_repo = MemoryRepository()
    for item in movie_set:
        movies_repo.add_movie(item)
    return movies_repo


def test_repository_can_add_a_movie(repo):
    movie = Movie("Moana", 2010)
    repo.add_movie(movie)
    assert repo.get_number_of_movies() == 6

def test_repository_can_retrieve_movie(repo):
    movie = repo.get_movie("Guardians of the Galaxy")
    assert movie.title == "Guardians of the Galaxy"

def test_repository_can_retrieve_movies_by_year(repo):
    movies_by_year = repo.get_movies_by_year(2016)
    assert len(movies_by_year) == 3

def test_repository_can_retrieve_all_movies(repo):
    movies = repo.get_all_movies()
    assert len(movies) == 5

def test_repository_can_retrieve_specified_movie_description(repo):
    description = repo.get_movie_description("Guardians of the Galaxy")
    assert description == 'A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.'

def test_repository_can_populate_repo(repo):
    repo.populate_repo('50movies.csv')
    assert len(repo.get_all_movies()) == 55

def test_repository_can_get_first_movie(repo):
    repo.populate_repo('50movies.csv')
    movie = repo.get_first_movies()
    assert len(movie) == 10
    assert movie[0].title == "5- 25- 77"

def test_repository_can_get_last_movie(repo):
    repo.populate_repo('50movies.csv')
    movie = repo.get_last_movies()
    assert len(movie) == 10
    assert movie[-1].title == "X-Men: Apocalypse"

def test_repository_can_get_next_movies(repo):
    repo.populate_repo('50movies.csv')
    movie = repo.get_first_movies()
    movie = repo.get_next_movies()
    assert len(movie) == 10
    assert movie[0].title == "Don't Fuck in the Woods"
    #Testing we can go to the next lot of 10 movies alphabetically
    movie = repo.get_next_movies()
    assert movie[0].title == "Interstellar"
    #Testing if we are on the last frame of movies, we can't go any further
    movie = repo.get_last_movies()
    movie = repo.get_next_movies()
    assert movie[0].title == "Suicide Squad"
    assert len(movie) == 10

def test_repository_can_get_previous_movies(repo):
    repo.populate_repo('50movies.csv')
    movie = repo.get_first_movies()
    movie = repo.get_previous_movies()
    #Testing if we are on first page, we can't go previous
    assert movie[0].title == "5- 25- 77"
    assert len(movie) == 10
    #Testing we can go previous page otherwise
    movie = repo.get_last_movies()
    movie = repo.get_previous_movies()
    assert movie[0].title == "Manchester by the Sea"
    assert len(movie) == 10
