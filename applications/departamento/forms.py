from django import forms
from applications.departamento.models import Departamento

class NewDepartamentoForm(forms.Form):
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=20)