import requests
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIRequestFactory
from ..views import TuoteList, TuoteDetail

"""
Ongelmia kirjautumisen kanssa? Kokeile tätä komennolla (muut unittest testit kannattaa kommentoida ensin pois): 

python manage.py test tuote.tests -v 2 

Jos testi toimii, katso vielä jos uusi luotu käyttäjä toimii.

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('admin', 'admin@example.com', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='admin', password='pass')
"""
factory = APIRequestFactory()

"""Tarkistaa että pyyntö onnistuu ja view:sin headers on text/html"""
def test_view_home_get():
    request = factory.get("/")
    response = TuoteList.as_view()(request)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"

def test_view_get():
    request = factory.get("/tuote/")
    response = TuoteList.as_view()(request)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"

def test_view_post(requesttuote):
    assert requesttuote.status_code == 201
    data = requesttuote.data

    assert data["id"] == 1
    assert data["nimi"] == "Django_APIRequestFactory"
    assert data["hinta"] == 4447777.0
    assert data["kuvaus"] == "Pla."
    assert data["tuotekuva"]


def test_view_put(tuote_factory):
    tuote_factory()

    payload = {
        "nimi": "Muokattu testi",
        "hinta": 999999444.0,
        "kuvaus": "Muokattu.",
        "tuotekuva": SimpleUploadedFile(name='puhelin.jpg', content=open("./tuote/tests/puhelin.jpg", 'rb').read(), content_type='image/jpeg')
    }

    request = factory.put("/tuote/1", payload)
    response = TuoteDetail.as_view()(request, pk=1)
    data = response.data

    assert data["id"] == 1
    assert data["nimi"] == "Muokattu testi"
    assert data["hinta"] == 999999444.0
    assert data["kuvaus"] == "Muokattu."
    assert data["tuotekuva"] is not None


def test_view_del(tuote_factory):
    tuote_factory()
    request = factory.delete("/tuote/1")
    response = TuoteDetail.as_view()(request, pk=1)
    assert response.status_code == 204
    

"""Tarkistaa jos nettisivu toimii sekä ensimmäisen tuotteen listassa"""
def test_url_get():
    url = "http://127.0.0.1:8000/tuote/"  

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