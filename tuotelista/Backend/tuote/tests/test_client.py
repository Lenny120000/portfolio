from rest_framework.test import APIClient
from django.forms.models import model_to_dict

client = APIClient()

def test_client_get():
    response = client.get("/")
    assert response.status_code == 200

    response = client.get("/tuote/")
    assert response.status_code == 200

def test_client_post(clienttuote):
    assert clienttuote.status_code == 201
    data = clienttuote.data

    assert data["id"] == 1
    assert data["nimi"] == "Django_APIClient"
    assert data["hinta"] == 4447777.0
    assert data["kuvaus"] == "Pla." 
    assert data["tuotekuva"] is not None

def test_client_put(tuote_factory):
    factory = tuote_factory()
    payload = model_to_dict(tuote_factory())

    response = client.put("/tuote/1", payload)
    data = response.data

    assert data["id"] == 1
    assert data["nimi"] == factory.nimi
    assert data["hinta"] == factory.hinta
    assert data["kuvaus"] == factory.kuvaus
    assert data["tuotekuva"] is not None

def test_client_del(tuote_factory):
    tuote_factory()
    response = client.delete("/tuote/1")
    assert response.status_code == 204
