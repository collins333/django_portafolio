from django.shortcuts import render, get_object_or_404
from .models import Publicacion

# Create your views here.
def home(request):
  publicaciones = Publicacion.objects.all()
  return render(request, 'publicacion.html', {'publicaciones': publicaciones})

def detalle(request, id):
  publicacion = get_object_or_404(Publicacion, pk=id)
  return render(request, 'detalle.html', {'publicacion': publicacion})
