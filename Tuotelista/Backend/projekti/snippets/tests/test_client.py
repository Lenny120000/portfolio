import json
from django.http import JsonResponse
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms.models import model_to_dict

class TestClient:

    client = APIClient()

    """Tarkistetaan jotta sivut "/" ja "/snippets/" toimivat """
    def test_client_get(self, client):
        response = client.get("/")
        assert response.status_code == 200

        response = client.get("/snippets/")
        assert response.status_code == 200


    """Luo uuden tuotteen /snippets/ sivussa ja tarkistaa kaikki tuotteen osat."""
    def test_client_post(self, clienttuote):
        assert clienttuote.status_code == 201
        data = clienttuote.data
        
        assert data["id"] == 1
        assert data["nimi"] == "Django_APIClient"
        assert data["hinta"] == 4447777.0
        assert data["kuvaus"] == "Pla." 
        assert data["tuotekuva"] is not None
        

    """Muokkaa tuotteen ja tarkistaa muutoksen."""
    def test_client_put(self, client, tuote_factory):
        factory = tuote_factory()
        print(factory.tuotekuva)

        payload = model_to_dict(tuote_factory())
        print(payload)

        response = client.put("/snippets/1", payload, format='multipart', content_type='multipart/form-data')
        print(response)
        
        data = response.data
        print(data)


        assert data["id"] == 1
        assert data["nimi"] == factory.nimi
        assert data["hinta"] == factory.hinta
        assert data["kuvaus"] == factory.kuvaus
        assert data["tuotekuva"] is not None

    """Poistaa tuotteen ja tarkistaa sen tapahtuvan."""
    def test_client_del(self, client, tuote_factory):
        tuote_factory()
        response = client.delete("/snippets/1")
        assert response.status_code == 204
