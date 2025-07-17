from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# models
from .models import Empleado
# forms
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    """"Vista que carga la página de inicio"""
    template_name = 'inicio.html'

# 1.- Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    """"Lista todos los empleados"""
    template_name = 'empleados/list_all.html'
    paginate_by = 4
    ordering = ['first_name']
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        print("lista resultado:", lista)
        return lista

# Listar empleados y poder editar o eliminar
class ListaEmpleadosAdmin(ListView):
    """"Lista todos los empleados"""
    template_name = 'empleados/lista_empleados.html'
    paginate_by = 10
    ordering = ['first_name']
    context_object_name = 'empleados'
    model = Empleado

# 2.- Listar todos los empleados que pertenecen a una área de la empresa
class ListByAreaEmpleado(ListView):
    """"Lista empleados de un área"""
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'

    #queryset = Empleado.objects.filter(
    #    departamento__shortname='contabilidad'
    #)

    def get_queryset(self):
        area=self.kwargs.get('shortname')
        lista =  Empleado.objects.filter(
            departamento__shortname=area
        )
        return lista

# 3.- Listar empleados por trabajo
class ListByJob(ListView):
    """"Lista empleados en un trabajo"""
    template_name = 'empleados/list_by_job.html'

    def get_queryset(self):
        trabajo=self.kwargs.get('job')
        lista = Empleado.objects.filter(
            job=trabajo
        )
        return lista

# 4.- Listar empleados por palabras clave
class ListEmpleadosByKWord(ListView):
    """"Lista empleados por palabra clave"""
    template_name = 'empleados/list_by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('****************')
        palabra_clave=self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        print("lista resultado:", lista)
        return lista

# 5.- Listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    """"Lista empleados por habilidades"""
    template_name = 'empleados/list_by_habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        #id_empleado= self.request.GET.get('kword', '')
        #id_empleado_int = int(id_empleado)
        empleado = Empleado.objects.get(id=5)
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleados/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #Todo un proceso
        context['titulo']='Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = 'empleados/success.html'

class EmpleadoCreateView(CreateView):
    template_name = 'empleados/add.html'
    model = Empleado
    form_class = EmpleadoForm

    success_url = reverse_lazy('empleados_app:empleados_admin')

    def form_valid(self, form):
        #Logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = 'empleados/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('************Metodo Post*********')
        print(request.POST)
        print(request.POST['last_name'])
        return super(EmpleadoUpdateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        #Logica del proceso
        print('************Metodo Form Valid*********')
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/delete.html'
    success_url = reverse_lazy('empleados_app:empleados_admin')

class SuccessDeletedView(TemplateView):
    template_name = 'empleados/success-deleted.html'












