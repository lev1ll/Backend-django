from django.shortcuts import render
from rest_framework import viewsets 
from .serializer import NacionalidadSerializer, ComunaSerializer,DireccionSerializer,LibroSerializer,LectorSerializer,PrestamoSerializer,AutorSerializer, BibiliotecaSerializer,TipoCategoriaSerializer,CategoriaSerializer
from .models import Nacionalidad,Comuna,Direccion,Lector,Libro,Autor,Prestamo,Biblioteca,TipoCategoria,Categoria

def pagina_inicio(request):
    return render(request, 'primera_app/inicio.html')



# Create your views here.

class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibiliotecaSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
