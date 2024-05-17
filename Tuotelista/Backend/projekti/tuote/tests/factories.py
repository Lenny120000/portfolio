import factory
from ..models import TuoteModel
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile

class TuoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TuoteModel

    nimi = "test_django_factory"
    hinta = 100
    kuvaus = "tehtaasta tuotettu"
    tuotekuva = ContentFile(
            open("./tuote/tests/widetest.jpg", "rb").read(),
            name=f"{timezone.now().timestamp()}.jpeg",
        )
    #SimpleUploadedFile(name='puhelin.jpg', content=open("./tuote/tests/puhelin.jpg", 'rb').read(), content_type='image/jpeg')
    #factory.django.ImageField()