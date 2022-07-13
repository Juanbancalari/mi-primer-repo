from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Equipo
from mi_app.models import Familia
from mi_app.forms import CursoBusquedaFormulario, CursoFormulario, EquipoFormulario, EquipoBusquedaFormulario

def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola mundo,{fecha_hora_ahora}")

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

        print(mi_formulario)


        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            curso = Curso(nombre=datos["curso"], camada=datos["camada"])   
            curso.save()

            return render(request, "mi_app/inicio.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = CursoFormulario()

    return render(request, "mi_app/curso_formulario.html", {"mi_formulario":mi_formulario})
def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()


    if request.GET:      
        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario, "cursos": cursos})


    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})

def busquedaCamada(request):

    return render(request, "mi_app/busquedaCamada.html")

def buscar(request):

    if request.GET['camada']:

        camada= request.GET['camada']
        cursos= Curso.objects.filter(camada__icontains=camada)

        return render(request, "mi_app/inicio.html", {"cursos":cursos, "camada":camada})
    else: 

        respuesta="No enviaste datos"
    
    #respuesta= f"Estoy buscando la camada nro: {request.GET ['camada']}"
    
    #return HttpResponse(respuesta)
    return render(request, "mi_app/inicio.html", {"respuesta":respuesta})
    
def formulario_equipo(request):#formulario_curso = formulario_equipo

    if request.method == "POST":

        mi_equipo = EquipoFormulario(request.POST)

        print(mi_equipo)


        if  mi_equipo.is_valid:
            datos = mi_equipo.cleaned_data 
            equipo = Equipo(nombre=datos["equipo"], posicion=datos["posicion"])   
            equipo.save()

            return render(request, "mi_app/equipo_formulario.html", {"mensaje":"agregado con exito!"})
    else:

        mi_equipo = EquipoFormulario()

    return render(request, "mi_app/equipo_formulario.html", {"mi_equipo":mi_equipo})

def formulario_busqueda_equipo(request):

    busqueda_formulario_equipo = EquipoBusquedaFormulario()


    if request.GET:      
        equipos = Equipo.objects.filter(nombre=busqueda_formulario_equipo["criterio"]).all()
        return render(request, "mi_app/equipo_busqueda.html", {"busqueda_formulario_equipo": busqueda_formulario_equipo, "equipos": equipos})


    return render(request, "mi_app/equipo_busqueda.html", {"busqueda_formulario_equipo": busqueda_formulario_equipo})        

def busquedaPosicion(request):

    return render(request, "mi_app/busquedaPosicion.html")

def buscar_equipo(request):

    if request.GET['posicion']:

        posicion= request.GET['posicion']
        equipos= Equipo.objects.filter(posicion__icontains=posicion)

        return render(request, "mi_app/inicio.html", {"equipos":equipos, "posicion":posicion})
    else: 

        respuesta="No enviaste datos"
    
    #respuesta= f"Estoy buscando la camada nro: {request.GET ['camada']}"
    
    #return HttpResponse(respuesta)
    return render(request, "mi_app/inicio.html", {"respuesta":respuesta})