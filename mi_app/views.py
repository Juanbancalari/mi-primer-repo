from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso
from mi_app.models import Familia
from mi_app.forms import CursoBusquedaFormulario, CursoFormulario

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
    


