from django.shortcuts import render, redirect, get_object_or_404
from .models import Comuna
from .forms import ComunaForm

def listado_comunas(request):
    comunas = Comuna.objects.all()
    return render(request, 'list.html', {'comunas': comunas})

def nueva_comuna(request):
    form = ComunaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listado_comunas')
    return render(request, 'form.html', {'form': form})

def editar_comuna(request, pk):
    comuna = get_object_or_404(Comuna, pk=pk)
    form = ComunaForm(request.POST or None, instance=comuna)
    if form.is_valid():
        form.save()
        return redirect('listado_comunas')
    return render(request, 'form.html', {'form': form})

def eliminar_comuna(request, pk):
    comuna = get_object_or_404(Comuna, pk=pk)
    if request.method == "POST":
        comuna.delete()
        return redirect('listado_comunas')
    return render(request, 'confirm_delete.html', {'comuna': comuna})
