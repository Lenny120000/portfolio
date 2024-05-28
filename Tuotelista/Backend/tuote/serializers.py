from rest_framework import serializers
from .models import TuoteModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    tuote = serializers.PrimaryKeyRelatedField(many=True, queryset=TuoteModel.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'tuote']

class TuoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = TuoteModel
        fields = ['id', 'nimi', 'hinta', 'kuvaus', 'tuotekuva', 'owner']
