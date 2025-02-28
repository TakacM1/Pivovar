from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('test', views.index, name='index2'),
    path('m1/', views.m1, name='m1'),
    path('m2/', views.m2, name='m2'),
]