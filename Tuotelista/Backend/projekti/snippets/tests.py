import requests
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
import pytest
import json

from .views import TuoteList
from snippets.models import Tuote

"""
Tee tämä jossain vaiheessa?

def test_post():
    factory = APIRequestFactory()
    obj = {
            "nimi": "Django testi loi tämän",
            "hinta": 7575757.0,
            "kuvaus": "Baabaa.",
            "tuotekuva": "http://127.0.0.1:8000/media/widetest_j8NnMq7.jpg"
        }
        
    request = factory.post('/snippets/', obj, format="json" )

    assert(request)
"""


@pytest.mark.django_db
def test_home_view():
    client = APIClient()
    response = client.get("/")
    print(response)
    assert response.status_code == 200

@pytest.mark.django_db
def test_getlist():
    client = APIClient()
    response = client.get("/snippets/")
    print(response)
    assert response.status_code == 200

@pytest.mark.django_db
def test_getlist():
    client = APIClient()
    response = client.get("/olemassa/")
    print(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_postlist():
    client = APIClient()
    response = client.post(

    {
        "id": 47,
        "nimi": "Playwright muokkasi tämän",
        "hinta": 12121212.0,
        "kuvaus": "Plapla.",
        "tuotekuva": "http://127.0.0.1:8000/media/widetest_j8NnMq7.jpg"
    }
    
    )
    assert response.status_code == 200



"""Tarkistaa että pyyntö on onnistuu ja view:sin headers on text/html"""
@pytest.mark.django_db
def test_factory_get():
    
    factory = APIRequestFactory()
    request = factory.get("/snippets/")
    response = TuoteList.as_view()(request)

    """
    Tämäkin jossain vaiheessa?
        try:
            tuote = Snippet.objects.get()
            print(tuote)
        except Snippet.DoesNotExist:
            tuote = None
            print("Ei toimi")
    """


    assert response.status_code, 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"


"""Tarkistaa jos nettisivu toimii sekä ensimmäisen tuotteen listassa"""
def test_url_get():
    
    url = "http://127.0.0.1:8000/snippets/"  
    response = requests.get(url)

    assert response.status_code == 200 
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert isinstance(data[0], dict)
    assert "id" in data[0]
    assert "nimi" in data[0]
    assert "hinta" in data[0]
    assert "kuvaus" in data[0]
    assert "tuotekuva" in data[0]