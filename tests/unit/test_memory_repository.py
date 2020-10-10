
import pytest
from webapp.domain.model import MovieFileCSVReader, Movie
from webapp.adapters.memory_repository import MemoryRepository



def test_repository_can_add_a_movie(in_memory_repo):
    movie = Movie("Moana", 2010)
    in_memory_repo.add_movie(movie)
    assert in_memory_repo.get_number_of_movies() == 51

def test_repository_can_retrieve_movie(in_memory_repo):
    movie = in_memory_repo.get_movie("Guardians of the Galaxy")
    assert movie.title == "Guardians of the Galaxy"

def test_repository_can_retrieve_movies_by_year(in_memory_repo):
    movies_by_year = in_memory_repo.get_movies_by_year(2016)
    assert len(movies_by_year) == 44

def test_repository_can_retrieve_all_movies(in_memory_repo):
    movies = in_memory_repo.get_all_movies()
    assert len(movies) == 50

def test_repository_can_retrieve_specified_movie_description(in_memory_repo):
    description = in_memory_repo.get_movie_description("Guardians of the Galaxy")
    assert description == 'A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.'

def test_repository_can_populate_repo(in_memory_repo):
    assert len(in_memory_repo.get_all_movies()) == 50

def test_repository_can_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movies()
    assert len(movie) == 10
    assert movie[0].title == "5- 25- 77"

def test_repository_can_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movies()
    assert len(movie) == 10
    assert movie[-1].title == "X-Men: Apocalypse"

def test_repository_can_get_next_movies(in_memory_repo):
    movie = in_memory_repo.get_first_movies()
    movie = in_memory_repo.get_next_movies()
    assert len(movie) == 10
    assert movie[0].title == "Don't Fuck in the Woods"
    #Testing we can go to the next lot of 10 movies alphabetically
    movie = in_memory_repo.get_next_movies()
    assert movie[0].title == "Jason Bourne"
    #Testing if we are on the last frame of movies, we can't go any further
    movie = in_memory_repo.get_last_movies()
    movie = in_memory_repo.get_next_movies()
    assert movie[0].title == "Suicide Squad"
    assert len(movie) == 10

def test_repository_can_get_previous_movies(in_memory_repo):
    movie = in_memory_repo.get_first_movies()
    movie = in_memory_repo.get_previous_movies()
    #Testing if we are on first page, we can't go previous
    assert movie[0].title == "5- 25- 77"
    assert len(movie) == 10
    #Testing we can go previous page otherwise
    movie = in_memory_repo.get_last_movies()
    movie = in_memory_repo.get_previous_movies()
    assert movie[0].title == "Jason Bourne"
    assert len(movie) == 10