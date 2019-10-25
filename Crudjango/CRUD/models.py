# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ListaLibros(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.ImageField()
    autor = models.CharField(max_length=100)
