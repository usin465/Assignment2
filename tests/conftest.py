import os
import pytest
from webapp import create_app
from webapp.adapters import memory_repository
from webapp.adapters.memory_repository import MemoryRepository
from webapp.domain.model import MovieFileCSVReader

TEST_DATA_PATH = "/Users/Uday/Desktop/235_WebApp/tests/data/50movies.csv"


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    repo.populate_repo(TEST_DATA_PATH)
    return repo


@pytest.fixture
def client():
    my_app = create_app({'TESTING':True,'TEST_DATA_PATH':TEST_DATA_PATH})
    return my_app.test_client()


