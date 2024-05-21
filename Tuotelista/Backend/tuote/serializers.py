from rest_framework import serializers
from .models import TuoteModel, LANGUAGE_CHOICES, STYLE_CHOICES

class TuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuoteModel
        fields = ['id', 'nimi', 'hinta', 'kuvaus', 'tuotekuva']
