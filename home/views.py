# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def onas(request):
    return render(request, 'onas.html')
