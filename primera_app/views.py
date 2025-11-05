from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
import django_filters
from .serializer import NacionalidadSerializer, ComunaSerializer, DireccionSerializer, LibroSerializer, LectorSerializer, PrestamoSerializer, AutorSerializer, BibliotecaSerializer, TipoCategoriaSerializer, CategoriaSerializer
from .models import Nacionalidad, Comuna, Direccion, Lector, Libro, Autor, Prestamo, Biblioteca, TipoCategoria, Categoria


# Acá creo los filtros para poder buscar libros por categoría o por autor
class LibroFilter(django_filters.FilterSet):
    id_categoria = django_filters.ModelChoiceFilter(
        queryset=Categoria.objects.all(),
        label='Categoría'
    )
    id_autor = django_filters.ModelChoiceFilter(
        queryset=Autor.objects.all(),
        label='Autor'
    )

    class Meta:
        model = Libro
        fields = ['id_categoria', 'id_autor']


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

# Esta vista muestra el listado de libros y permite filtrarlos
@login_required
def listado_libros(request):
    f = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(request, 'primera_app/lista_libros.html', {'filter': f})

# Acá creo los ViewSets para la API REST - cada uno maneja el CRUD de su modelo
class NacionalidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class AutorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class LectorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer