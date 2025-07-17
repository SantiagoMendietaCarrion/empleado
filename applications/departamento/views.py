from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from applications.empleados.models import Empleado, Habilidades
from .models import Departamento
from django.urls import reverse_lazy

# Create your views here.
class DepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    model = Departamento
    context_object_name = 'departamentos'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:departamento_list')

    def form_valid(self, form):
        print("**********Estamos en el form valid***************")
        # Crear y guardar departamento. Mediante una forma
        depa = Departamento(name=form.cleaned_data['departamento'], shortname=form.cleaned_data['shortname'])
        depa.save()
        # Crear y guardar empleado. Mediante otra forma
        nombres = form.cleaned_data['nombres']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(first_name=nombres, last_name=apellidos, job=1, departamento=depa)
        return super(NewDepartamentoView, self).form_valid(form)


