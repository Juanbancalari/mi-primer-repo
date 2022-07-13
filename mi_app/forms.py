from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    

class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

class EquipoFormulario(forms.Form):
    equipo = forms.CharField()
    posicion = forms.IntegerField()
    email= forms.EmailField()

class EquipoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()    