from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    my_profil = MyProfil.objects.all()
    context = {
        "my_profil":my_profil
    }
    return render(request, 'home.html', context)
