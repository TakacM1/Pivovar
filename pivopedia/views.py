from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pedia(request):
    return render(request, 'pedia.html')
