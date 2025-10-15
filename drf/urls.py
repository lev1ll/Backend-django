from django.contrib import admin
from django.urls import path, include
from primera_app import views as app_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API de Biblioteca",
      default_version='v1',
      description="Documentación de la API para el proyecto de biblioteca.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contacto@tuproyecto.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('primera_app.urls')),
    path('', app_views.pagina_inicio, name='home'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('registro/', app_views.registro, name='registro'),
    
    # --- ESTA ES LA LÍNEA CORREGIDA ---
    path('accounts/', include('django.contrib.auth.urls')),
]