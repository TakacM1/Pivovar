from django.shortcuts import render
from django.http import HttpResponse
from .models import VydricaVYCAP, RozadolVYCAP

# Create your views here.

def ponuka(request):

    Vyd = VydricaVYCAP.objects.all()
    Roz = RozadolVYCAP.objects.all()
    
    return render(request, 'ponuka.html', {'Vyd': Vyd, 'Roz': Roz})

