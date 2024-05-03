from rest_framework import serializers
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Tuote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nimi = models.TextField(default='')
    hinta = models.FloatField(default=0)
    kuvaus = models.TextField(default='')
    tuotekuva = models.ImageField(default='')

    class Meta:
        ordering = ['created']