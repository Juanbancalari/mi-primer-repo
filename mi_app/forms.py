from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    email = forms.EmailField()

class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()