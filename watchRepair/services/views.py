from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView
from .models import Service

# Create your views here.
# Vista para listar servicios
class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'
