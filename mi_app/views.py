from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Equipo
from mi_app.models import Familia
from mi_app.forms import CursoBusquedaFormulario, CursoFormulario, EquipoBusquedaFormulario, EquipoFormulario

def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola mundo,{fecha_hora_ahora}")

def calcular_imc(request):
    context = {
        "imc": 0
    }
    if request.GET:
        altura= float(request.GET["altura"])
        peso= float(request.GET["peso"])

        context["imc"] = peso /(altura * altura)
    return render(request, "mi_app/imc.html", context)

def listar_cursos(request):
    context=  {}

    context ["cursos"]= Curso.objects.all()

    return render(request, "mi_app/lista_cursos.html", context)

def listar_familia(request):

    context= {}

    context ["familias"]= Familia.objects.all()

    return render(request, "mi_app/mi_familia.html", context)

def formulario_curso(request):

    if request.method == "POST":

        mi_formulario = CursoFormulario(request.POST)

        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()

            return render(request, "mi_app/curso_formulario.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = CursoFormulario()

    return render(request, "mi_app/curso_formulario.html", {"mi_formulario":mi_formulario})



def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()


    if request.GET:      
        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario, "cursos": cursos})


    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})


    

def listar_equipos(request):
    context=  {}

    context ["equipos"]= Equipo.objects.all()

    return render(request, "mi_app/lista_equipos.html", context)

def formulario_equipo(request):

    if request == "POST":
        mi_formulario_equipo= EquipoFormulario(request.POST)

        if mi_formulario_equipo.is_valid:

            datos= mi_formulario_equipo.cleaned_data
            equipo = Equipo(nombre=datos["nombre"], posicion=datos["posicion"])
            equipo.save()

            return render(request, "mi_app/equipo_formulario.html", {"mensaje":"agregado con exito!"})
    else:
        mi_formulario_equipo =  EquipoFormulario()
    return render(request, "mi_app/equipo_formulario.html", {"mi_formulario_equipo": mi_formulario_equipo})

def formulario_busqueda_equipo(request):

    busqueda_formulario_equipo = EquipoBusquedaFormulario()


    if request.GET:      
        equipos = Equipo.objects.filter(nombre=busqueda_formulario_equipo["criterio"]).all()
        return render(request, "mi_app/equipo_busqueda.html", {"busqueda_formulario_equipo": busqueda_formulario_equipo, "equipos": equipos})
    
    
    return render(request, "mi_app/equipo_busqueda.html", {"busqueda_formulario_equipo": busqueda_formulario_equipo})
