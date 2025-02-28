# home/models.py
from django.db import models

class VydricaVYCAP(models.Model):
    povod = models.CharField(max_length=100)
    nazov = models.CharField(max_length=100)
    styl = models.CharField(max_length=100)
    plato = models.CharField(max_length=10)
    alkohol = models.CharField(max_length=10)
    price_05l = models.CharField(max_length=5, default='/')
    price_04l = models.CharField(max_length=5, default='/')
    price_03l = models.CharField(max_length=5, default='/')
    price_02l = models.CharField(max_length=5, default='/')

    def __str__(self):
        return f"{self.nazov}"

class RozadolVYCAP(models.Model):
    povod = models.CharField(max_length=100)
    nazov = models.CharField(max_length=100)
    styl = models.CharField(max_length=100)
    plato = models.CharField(max_length=10)
    alkohol = models.CharField(max_length=10)
    price_05l = models.CharField(max_length=5, default='/')
    price_04l = models.CharField(max_length=5, default='/')
    price_03l = models.CharField(max_length=5, default='/')
    price_02l = models.CharField(max_length=5, default='/')

    def __str__(self):
        return f"{self.nazov}"
