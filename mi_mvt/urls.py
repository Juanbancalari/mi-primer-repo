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
from mi_app.views import  listar_cursos, listar_familia, formulario_curso, buscar, busquedaCamada, formulario_equipo, buscar_equipo, busquedaPosicion, formulario_busqueda_equipo


urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludar/",saludo),
    path("listar-cursos/", listar_cursos),
    path("listar-familia/", listar_familia), 
    path("formulario/", formulario_curso),
    #path("buscar/", formulario_busqueda),
    path("buscar/", buscar),
    path("busquedaCamada/", busquedaCamada),
    path("buscar-equipo/", buscar_equipo),
    path("busquedaPosicion/", busquedaPosicion),
    path("formulario-equipo/", formulario_equipo),
    path("formulario-busqueda-equipo/", formulario_busqueda_equipo)
    
    
    
]
