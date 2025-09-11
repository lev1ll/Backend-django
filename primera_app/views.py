from django.shortcuts import render
from rest_framework import viewsets 
from .serializer import Nacionalidad_Serializer, Comuna_Serializer,Direccion_Serializer,Libro_Serializer,Lector_Serializer,Prestamo_Serializer,Autor_Serializer, Bibilioteca_Serializer,TipoCategoria_Serializer,Categoria_Serializer
from .models import Nacionalidad,Comuna,Direccion,Lector,Libro,Autor,Prestamo,Biblioteca,TipoCategoria,Categoria


# Create your views here.

class Nacionalidad_ViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = Nacionalidad_Serializer


class Autor_ViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = Autor_Serializer


class Comuna_ViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer


class Direccion_ViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = Direccion_Serializer


class Biblioteca_ViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = Bibilioteca_Serializer


class Libro_ViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = Libro_Serializer


class Lector_ViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = Lector_Serializer


class Prestamo_ViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = Prestamo_Serializer

class TipoCategoria_ViewSet(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoria_Serializer

class Categoria_ViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = Categoria_Serializer
