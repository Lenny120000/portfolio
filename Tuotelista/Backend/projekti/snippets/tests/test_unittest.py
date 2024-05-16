import shutil
from django.conf import settings
from django.utils import timezone

from rest_framework.test import APITestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms.models import model_to_dict
from django.core.files.base import ContentFile

from snippets.models import Tuote

# where all the test images are sent
TEST_DIR = "testmedia"


class TestUnittest(APITestCase):
    """Tarkistetaan jotta sivut "/" ja "/snippets/" toimivat"""

    # changes media folder to test folder so that test pictures are kept separate from real images
    @override_settings(MEDIA_ROOT=TEST_DIR)
    def setUp(self):
        # sets up database with products before test starts and creates test image
        self.test_product = Tuote.objects.create(
            nimi="pölymonsteri",
            kuvaus="imee pikkupölyjä",
            hinta=2.50,
            tuotekuva=ContentFile(
            open("./snippets/tests/puhelin.jpg", "rb").read(),
            name=f"{timezone.now().timestamp()}.jpeg",
            )
        )
        self.test_product1 = Tuote.objects.create(
            nimi="dustsucker 9000",
            kuvaus="imee kaiken kuiviin",
            hinta=420,
            tuotekuva=ContentFile(
            open("./snippets/tests/widetest.jpg", "rb").read(),
            name=f"{timezone.now().timestamp()}.jpeg",
            )
        )
        self.test_image1 = ContentFile(
            open("./snippets/tests/widetest.jpg", "rb").read(),
            name=f"{timezone.now().timestamp()}.jpeg",
        )

    def test_client_get(self):

        response = self.client.get("/")
        assert response.status_code == 200

        response = self.client.get("/snippets/")
        assert response.status_code == 200

    """Luo uuden tuotteen /snippets/ sivussa ja tarkistaa kaikki tuotteen osat."""

    @override_settings(MEDIA_ROOT=TEST_DIR)
    def test_client_post(self):
        payload = {
            "nimi": "Django_APIClient",
            "hinta": 4447777.0,
            "kuvaus": "Pla.",
            "tuotekuva": self.test_image1,
        }

        response = self.client.post("/snippets/", payload)
        assert response.status_code == 201
        data = response.data

        assert data["nimi"] == "Django_APIClient"
        assert data["hinta"] == 4447777.0
        assert data["kuvaus"] == "Pla."
        assert data["tuotekuva"] is not None

    """Muokkaa tuotteen ja tarkistaa muutoksen."""

    @override_settings(MEDIA_ROOT=TEST_DIR)
    def test_client_put(self):

        payload = {
            "nimi": "test_django_factory",
            "hinta": 100,
            "kuvaus": "tehtaasta tuotettu",
            "tuotekuva": self.test_image1,
        }

        response = self.client.put(
            "/snippets/1",
            payload,
            format="multipart",
        )

        data = response.data
        assert data["id"] == 1
        assert data["nimi"] == payload["nimi"]
        assert data["hinta"] == payload["hinta"]
        assert data["kuvaus"] == payload["kuvaus"]
        assert data["tuotekuva"] is not None

    """Poistaa tuotteen ja tarkistaa sen tapahtuvan."""

    def test_client_del(self):
        response = self.client.delete("/snippets/1")
        assert response.status_code == 204

    # removes test media folder after all tests are done
    @classmethod
    def tearDownClass(self):
        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass
        super().tearDownClass()
