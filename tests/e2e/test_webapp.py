import pytest
from flask import session

def test_index(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200
    assert b'MovieBase' in response.data

def test_browse_movies(client):
    response = client.get('/browse_movies')
    assert response.status_code == 200

def test_get_last_movies(client):
    response = client.get('/browse_movies/last')
    assert response.status_code == 200

def test_get_first_movies(client):
    response = client.get('/browse_movies/first')
    assert response.status_code == 200
