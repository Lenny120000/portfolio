import pytest
from pytest_factoryboy import register
from django.core.files.uploadedfile import SimpleUploadedFile
from .factories import TuoteFactory
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from ..views import TuoteList

client = APIClient()
factory = APIRequestFactory()


register(TuoteFactory)

@pytest.fixture()
def clienttuote():

    payload = {
        "nimi": "Django_APIClient",
        "hinta": 4447777.0,
        "kuvaus": "Pla.",
        "tuotekuva": SimpleUploadedFile(name='widetest.jpg', content=open("./tuote/tests/widetest.jpg", 'rb').read(), content_type='image/jpeg')
    }

    response = client.post("/tuote/", payload)
    return response

@pytest.fixture()
def requesttuote():

    payload = {
        "nimi": "Django_APIRequestFactory",
        "hinta": 4447777.0,
        "kuvaus": "Pla.",
        "tuotekuva": SimpleUploadedFile(name='widetest.jpg', content=open("./tuote/tests/widetest.jpg", 'rb').read(), content_type='image/jpeg')
    }
    request = factory.post('/tuote/', payload)
    response = TuoteList.as_view()(request)
    return response

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass