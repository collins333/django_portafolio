from django.shortcuts import render
from .models import Portafolio

def index(request):
  return render(request, 'index.html')

def home(request):
  portafolios = Portafolio.objects.all()
  return render(request, 'home.html', {'portafolios': portafolios})