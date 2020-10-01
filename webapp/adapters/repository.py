import abc
from typing import List
from datetime import date

from webapp.domain.model import Genre, Actor, Movie,Director, Review, User, WatchList, MovieFileCSVReader
repo_instance = None
class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie_name) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_year(self, year) -> List[Movie]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_description(self):
        raise NotImplementedError

    @abc.abstractmethod
    def populate_repo(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_next_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_previous_movies(self):
        raise NotImplementedError

    #@abc.abstractmethod
    #def get_next_frame(self):
        #raise NotImplementedError

    #@abc.abstractmethod
    #def get_previous_frame(self):
        #raise NotImplementedError


    #@abc.abstractmethod
    #def get_movie_description(self, movie_name):
        #raise NotImplementedError


    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self, genre_type) -> Genre:
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self, actor_name) -> Actor:
        raise NotImplementedError


    #@abc.abstractmethod
    #def get_movies_by_release_year(self, target_date: int) -> List[Movie]:
        #raise NotImplementedError

    #@abc.abstractmethod
    #def get_movies_by_director(self, director: Director) -> List[Movie]:
        #raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        raise NotImplementedError

    #@abc.abstractmethod
    #def get_first_movie(self) -> Movie:
        #raise NotImplementedError

    #@abc.abstractmethod
    #def get_last_movie(self) -> Movie:
        #raise NotImplementedError

    #@abc.abstractmethod
    #def get_review(self) -> Review:
        #raise NotImplementedError
    #@abc.abstractmethod
    #def get_user(self, username) -> User:
        #raise NotImplementedError

    #@abc.abstractmethod
    #def add_user(self, user: User):
        #raise NotImplementedError

    #@abc.abstractmethod
    #def add_watchlist(self, watchlist: WatchList):
        #raise NotImplementedError

    #@abc.abstractmethod
    #def get_watchlist(self, watchlist) -> WatchList:
        #raise NotImplementedError








