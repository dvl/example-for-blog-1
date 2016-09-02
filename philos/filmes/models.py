from __future__ import unicode_literals

from django.db import models


class Filme(models.Model):
    nome = models.CharField(max_length=255)
