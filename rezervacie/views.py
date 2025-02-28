from django.shortcuts import render
from django.http import HttpResponse
from .models import booking
# Create your views here.


def index(request):
    return render(request, 'index.html')

def lsb(request):
    """return HttpResponse('Takač testing')"""
    return render(request, 'index.html', {'name': 'Marcel'})

def m1(request):
    request.session['m'] = "DRAZDIAK"
    return render(request, 'm1.html')

def m2(request):
    request.session['m'] = "KUCHAJDA"
    return render(request, 'm2.html')

# Use 'm' in the form submission
def submit_form(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        mail = request.POST.get('email')
        date = request.POST.get('date')
        poznamka = request.POST.get('poznamka')

        # Retrieve 'm' from session
        m = request.session.get('m', "neurčene")  # Default to "neurčene" if not set

        # Process the data
        rezervacia = booking(Ffname=fname, Femail=mail, Fdate=date, Fpoznamka=poznamka, Foption=m)
        rezervacia.save()

        return render(request, 'prisla.html')

    else:
        return HttpResponse("Invalid request")