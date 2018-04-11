from os.path import join, dirname

import pytest


ROOT_DIR = dirname(dirname(__file__))

@pytest.fixture
def root_dir():
    return ROOT_DIR

@pytest.fixture
def test_file():
    def test_file_function(filename):
        return join(ROOT_DIR, 'tests/files', filename)
    return test_file_function
