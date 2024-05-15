import factory
from ..models import Tuote
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile

class TuoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tuote

    nimi = "test_django_factory"
    hinta = 100
    kuvaus = "tehtaasta tuotettu"
    tuotekuva = ContentFile(open("./snippets/tests/widetest.jpg", 'rb').read(), name='widetest.jpg')

    #SimpleUploadedFile(name='puhelin.jpg', content=open("./snippets/tests/puhelin.jpg", 'rb').read(), content_type='image/jpeg')
    #factory.django.ImageField()