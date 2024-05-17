import json
from django.http import JsonResponse
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms.models import model_to_dict

from django.utils import timezone
from django.core.files.base import ContentFile


class TestClient:

    client = APIClient()

    """Tarkistetaan jotta sivut "/" ja "/tuote/" toimivat """
    def test_client_get(self, client, tuote_factory):
        factory = tuote_factory()
        response = client.get("/")
        assert response.status_code == 200
        data = response.data[0]

        assert data["id"] == 1
        assert data["nimi"] == factory.nimi
        assert data["hinta"] == factory.hinta
        assert data["kuvaus"] == factory.kuvaus
        assert data["tuotekuva"] is not None


        response = client.get("/tuote/")
        assert response.status_code == 200
        data = response.data[0]

        assert data["id"] == 1
        assert data["nimi"] == factory.nimi
        assert data["hinta"] == factory.hinta
        assert data["kuvaus"] == factory.kuvaus
        assert data["tuotekuva"] is not None

    """Luo uuden tuotteen /tuote/ sivussa ja tarkistaa kaikki tuotteen osat."""
    def test_client_post(self, clienttuote):
        assert clienttuote.status_code == 201
        data = clienttuote.data
        
        assert data["id"] == 1
        assert data["nimi"] == "Django_APIClient"
        assert data["hinta"] == 4447777.0
        assert data["kuvaus"] == "Pla." 
        assert data["tuotekuva"] is not None
        

    """Poistaa tuotteen ja tarkistaa sen tapahtuvan."""
    def test_client_del(self, client, tuote_factory):
        tuote_factory()
        response = client.delete("/tuote/1")
        assert response.status_code == 204

    #HUOM! Ei toimi luokissa jostakin syystä.
    """ Muokkaa tuotteen ja tarkistaa muutoksen."""

    """
    def test_client_put(self, client, tuote_factory):
        print(ContentFile(
            open("./tuote/tests/widetest.jpg", "rb").read(),
            name=f"{timezone.now().timestamp()}.jpeg",
        ))
        factory = tuote_factory()

        payload = model_to_dict(tuote_factory())

        payload = {
            "nimi": "test_django_factory",
            "hinta": 100,
            "kuvaus": "tehtaasta tuotettu",
            "tuotekuva": ContentFile(
            open("./tuote/tests/widetest.jpg", "rb").read(),
            name=f"{timezone.now().timestamp()}.jpeg",
        ),
        }

        print(payload)

        response = client.put("/tuote/1", payload, format='multipart', content_type='multipart/form-data')
        print(response)
        
        data = response.data
        print(data)


        assert data["id"] == 1
        assert data["nimi"] == factory.nimi
        assert data["hinta"] == factory.hinta
        assert data["kuvaus"] == factory.kuvaus
        assert data["tuotekuva"] is not None
    """