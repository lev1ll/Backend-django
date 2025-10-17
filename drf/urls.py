from django.contrib import admin
from django.urls import path, include
from primera_app import views

# Configuración para la documentación de la API
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación API Mi_Aplicacion",
        default_version='v1',
        description="Mi_Aplicacion",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mi_correo@test.test"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name='home'),
    
    # URL's para aplicación particular
    path('primera_app/', include('primera_app.urls')),
    
    # URL's para documentación de API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # URL's de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),  
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'), 
]
