from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .serializer import NacionalidadSerializer, ComunaSerializer, DireccionSerializer, LibroSerializer, LectorSerializer, PrestamoSerializer, AutorSerializer, BibiliotecaSerializer, TipoCategoriaSerializer, CategoriaSerializer
from .models import Nacionalidad, Comuna, Direccion, Lector, Libro, Autor, Prestamo, Biblioteca, TipoCategoria, Categoria


def logout_view(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(
                request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def pagina_inicio(request):
    return render(request, 'primera_app/inicio.html')

# ViewSets para la API
class NacionalidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class AutorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Biblioteca.objects.all()
    serializer_class = BibiliotecaSerializer

class LectorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer