"""mi_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mi_app.views import saludo
from mi_app.views import calcular_imc, listar_cursos, listar_familia, formulario_curso, formulario_busqueda, listar_equipos, formulario_equipo, formulario_busqueda_equipo
from manejador_contenido.views import mostrar_home, mostrar_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludar/",saludo),
    path("imc/", calcular_imc),
    path("listar-cursos/", listar_cursos),
    path("listar-familia/", listar_familia),
    path("home/", mostrar_home),
    path("profile/", mostrar_profile),
    path("formulario/", formulario_curso),
    path("buscar/", formulario_busqueda),
    path("listar-equipos/", listar_equipos),
    path("formulario-equipo/", formulario_equipo),
    path("buscar-equipo/", formulario_busqueda_equipo),
    
]
