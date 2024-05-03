import pytest

@pytest.fixture()
def tuotelista():
    testituote = open("./fixtures/db.json", "r")
    db = testituote.read()
    return db
