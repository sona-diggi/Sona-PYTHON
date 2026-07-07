import pytest

@pytest.fixture
def username():
    return "admin"

@pytest.fixture
def password():
    return "1234"