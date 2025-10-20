from django.shortcuts import render, get_object_or_404, redirect
from .models import Clientes
from .forms import ClientesForm

def index(request):
    clientes = Clientes.objects.all()
    return render(request, 'index.html', {'clientes': clientes})

def ver_cliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    return render(request, 'ver_cliente.html', {'cliente': cliente})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClientesForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClientesForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('inicio')
    return render(request, 'borrar_cliente.html', {'cliente': cliente})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Clientes
from .forms import ClientesForm

def index(request):
    clientes = Clientes.objects.all()
    return render(request, 'index.html', {'clientes': clientes})

def ver_cliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    return render(request, 'ver_cliente.html', {'cliente': cliente})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_satisfactorio')
    else:
        form = ClientesForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('editar_satisfactorio')
    else:
        form = ClientesForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('inicio')
    return render(request, 'borrar_cliente.html', {'cliente': cliente})

def agregar_satisfactorio(request):
    return render(request, 'agregar_satisfactorio.html')

def editar_satisfactorio(request):
    return render(request, 'editar_satisfactorio.html')