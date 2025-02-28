# ponuka/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ponuka, name='ponuka'),
]
