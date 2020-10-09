import os
import pytest
from webapp import create_app
from webapp.adapters import memory_repository
from webapp.adapters.memory_repository import MemoryRepository
from webapp.domain.model import MovieFileCSVReader

TEST_DATA_PATH = "/Users/Uday/Desktop/235_WebApp/tests/unit/50movies.csv"

@pytest.fixture
def client():
    my_app = create_app({'TESTING':True,'TEST_DATA_PATH':TEST_DATA_PATH})
    return my_app.test_client()


