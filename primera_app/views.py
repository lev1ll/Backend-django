from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
# TUS imports con TUS modelos y serializers
from .serializer import NacionalidadSerializer, ComunaSerializer, DireccionSerializer, LibroSerializer, LectorSerializer, PrestamoSerializer, AutorSerializer, BibiliotecaSerializer, TipoCategoriaSerializer, CategoriaSerializer
from .models import Nacionalidad, Comuna, Direccion, Lector, Libro, Autor, Prestamo, Biblioteca, TipoCategoria, Categoria

# Vista de logout personalizada como el profesor
def logout_view(request):
    # Cierra la sesión del usuario y limpia la data de SESSION
    logout(request)
    # Redirige a la página de inicio de sesión
    return redirect('login')

# Vista de registro exacta como el profesor pero con tus templates
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
    return render(request, 'primera_app/registration/registro.html', {'form': form})

# Página de inicio - puedes elegir si quieres @login_required o no
def pagina_inicio(request):
    return render(request, 'primera_app/inicio.html')

# ViewSets con estructura del profesor pero TUS modelos
# Nota: Tu modelo se llama Nacionalidad, el del profesor también, pero con campos diferentes
class NacionalidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Nacionalidad.objects.all()  # TU modelo Nacionalidad
    serializer_class = NacionalidadSerializer  # TU serializer

class AutorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Autor.objects.all()  # TU modelo Autor
    serializer_class = AutorSerializer  # TU serializer

class ComunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Comuna.objects.all()  # TU modelo Comuna
    serializer_class = ComunaSerializer  # TU serializer

class DireccionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Direccion.objects.all()  # TU modelo Direccion
    serializer_class = DireccionSerializer  # TU serializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Biblioteca.objects.all()  # TU modelo Biblioteca
    serializer_class = BibiliotecaSerializer  # TU serializer

class LectorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Lector.objects.all()  # TU modelo Lector
    serializer_class = LectorSerializer  # TU serializer

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = TipoCategoria.objects.all()  # TU modelo TipoCategoria
    serializer_class = TipoCategoriaSerializer  # TU serializer

class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Categoria.objects.all()  # TU modelo Categoria
    serializer_class = CategoriaSerializer  # TU serializer

class LibroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Libro.objects.all()  # TU modelo Libro
    serializer_class = LibroSerializer  # TU serializer

class PrestamoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Prestamo.objects.all()  # TU modelo Prestamo
    serializer_class = PrestamoSerializer  # TU serializer