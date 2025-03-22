from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView
from .models import Service

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Vista para listar servicios

