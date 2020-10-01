import csv
import os
import datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash
from webapp.adapters.repository import AbstractRepository
from webapp.domain.model import Genre, Actor, Movie, Director, Review, User, WatchList, MovieFileCSVReader
from pathlib import Path


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = list()
        self._genres = list()
        self._actors = list()
        self._movies_release_year = dict()
        self._movies_director = dict()
        self._reviews = list()
        self._users = list()
        self._watchlist = list()
        self.frame_count = 10

    def add_movie(self, movie: Movie):
        self._movies.append(movie)
        self._movies.sort()

    def get_movie(self, movie_name) -> Movie:
        return next((movie for movie in self._movies if movie.title == movie_name), None)

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genre(self, genre_type) -> Genre:
        return next((genre for genre in self._genres if genre.genre_name == genre_type), None)

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actor(self, actor_name) -> Actor:
        return next((actor for actor in self._actors if actor.actor_full_name == actor_name), None)

    def get_number_of_movies(self):
        return len(self._movies)

    def get_movies_by_year(self, year: int):
        movies_by_year = []
        for movie in self._movies:
            if year == movie._release_year:
                movies_by_year.append(movie)
        return movies_by_year

    def get_all_movies(self):
        return self._movies

    def get_movie_description(self, movie_name):
        return next((movie.description for movie in self._movies if movie.title == movie_name), None)

    def populate_repo(self, filename:str):
        # filename = 'MovieWebApp/webapp/domain/movies.csv'
        #filename = 'webapp/domain/movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()
        movie_set = movie_file_reader.dataset_of_movies
        for movie in movie_set:
            self.add_movie(movie)
        self._movies.sort()

    def get_first_movies(self):
        self.frame_count = 10
        return list(self._movies[0:10])

    def get_last_movies(self):
        self.frame_count = len(self._movies) - 10
        return list(self._movies[-10:])

    def get_next_movies(self):
        if self.frame_count == len(self._movies)-10:
            return self.get_last_movies()
        else:
            self.frame_count += 10
            frame_start = self.frame_count - 10
            return self._movies[frame_start:self.frame_count]




    def get_previous_movies(self):
        if self.frame_count == 10:
            return self.get_first_movies()
        else:
            self.frame_count -= 10
            frame_start = self.frame_count - 10
            return self._movies[frame_start:self.frame_count]
