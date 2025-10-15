from django.shortcuts import render
from rest_framework import viewsets 
from .serializer import NacionalidadSerializer, ComunaSerializer,DireccionSerializer,LibroSerializer,LectorSerializer,PrestamoSerializer,AutorSerializer, BibiliotecaSerializer,TipoCategoriaSerializer,CategoriaSerializer
from .models import Nacionalidad,Comuna,Direccion,Lector,Libro,Autor,Prestamo,Biblioteca,TipoCategoria,Categoria
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

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

def registro(request):
    if request.method == 'POST':
        # Si el formulario se ha enviado, procesa los datos
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo usuario
            user = form.save()
            # Inicia sesión automáticamente para el nuevo usuario
            login(request, user)
            messages.success(request, "¡Registro exitoso! Has iniciado sesión.")
            return redirect('home') # Redirige a la página de inicio
        else:
            # Si el formulario no es válido, muestra los errores
            messages.error(request, "Hubo un error en el registro. Por favor, revisa los datos.")
    else:
        # Si es la primera vez que se visita la página, muestra un formulario vacío
        form = UserCreationForm()
    
    # Renderiza la plantilla HTML pasándole el formulario como contexto
    return render(request, 'primera_app/registration/registro.html', {'form': form})