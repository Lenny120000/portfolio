import json
from rest_framework.test import APIClient


class TestTuoteModel:
    endpoint = "/tuote/"
    client = APIClient()

    def test_model_get(self, tuote_factory):
        obj = tuote_factory()
        
        assert obj.id == 1
        assert obj.nimi == "test_django_factory"
        assert obj.hinta == 100
        assert obj.kuvaus == "tehtaasta tuotettu"
        assert obj.tuotekuva is not None
    
    def test_client_multiple_get(self, tuote_factory, client):
        tuote_factory.create_batch(5)

        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5