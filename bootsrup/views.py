from django.shortcuts import render
from .models import Caruosel

# Create your views here.
def index(request):
    carusel_data = Caruosel.objects.all()
    contex = {
        'carusel_data' : carusel_data
    }
    return render(request,'index.html',contex)
