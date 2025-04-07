from django.shortcuts import render, redirect
from .models import Empleado, Documento
from .forms import EmpleadoForm, DocumentoForm

def lista_empleados(request):
    empleados = Empleado.objects.all().order_by('id')  # O cualquier orden deseado
    return render(request, 'documents/lista_empleados.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documents:lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'documents/crear_empleado.html', {'form': form})

def crear_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents:lista_empleados')
    else:
        form = DocumentoForm()
    return render(request, 'documents/crear_documento.html', {'form': form})
