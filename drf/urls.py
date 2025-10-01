from django.contrib import admin
from django.urls import path, include
from primera_app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('primera_app.urls')),
    path('', app_views.pagina_inicio, name='home'),
]