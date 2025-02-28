# Register your models here.
# home/admin.py
from django.contrib import admin
from .models import VydricaVYCAP, RozadolVYCAP

@admin.register(VydricaVYCAP)
class VydricaAdmin(admin.ModelAdmin):
    list_display = ('povod', 'nazov', 'styl', 'plato', 'alkohol', 'price_05l', 'price_04l', 'price_03l', 'price_02l')

@admin.register(RozadolVYCAP)
class RozadolAdmin(admin.ModelAdmin):
    list_display = ('povod', 'nazov', 'styl', 'plato', 'alkohol', 'price_05l', 'price_04l', 'price_03l', 'price_02l')
