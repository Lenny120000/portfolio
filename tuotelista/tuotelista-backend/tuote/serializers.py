from rest_framework import serializers
from .models import TuoteModel
from django.contrib.auth.models import User


class TuoteSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = TuoteModel
        fields = ['id', 'nimi', 'hinta', 'kuvaus', 'tuotekuva'] #', owner'

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    tuote = serializers.HyperlinkedRelatedField(many=True, view_name='tuote-detail', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'tuote']

class LoginSerializer(serializers.Serializer):
    nimi = serializers.CharField()
    salasana = serializers.CharField()
"""
