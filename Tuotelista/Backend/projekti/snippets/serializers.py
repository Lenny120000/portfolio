from rest_framework import serializers
from .models import Tuote, LANGUAGE_CHOICES, STYLE_CHOICES

class TuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuote
        fields = ['id', 'nimi', 'hinta', 'kuvaus', 'tuotekuva']
