# ponuka/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedia, name='pedia'),
]
