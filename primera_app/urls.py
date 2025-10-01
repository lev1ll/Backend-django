from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'nacionalidades', views.NacionalidadViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'comunas', views.ComunaViewSet)
router.register(r'direcciones', views.DireccionViewSet)
router.register(r'bibliotecas', views.BibliotecaViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'lectores', views.LectorViewSet)
router.register(r'prestamos', views.PrestamoViewSet)
router.register(r'tipos-categoria', views.TipoCategoriaViewSet)
router.register(r'categorias', views.CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]