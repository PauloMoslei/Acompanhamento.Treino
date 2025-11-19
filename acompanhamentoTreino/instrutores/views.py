from django.shortcuts import render, get_object_or_404, redirect
from .models import Instrutor
from .forms import InstrutorForm

def lista_instrutores(request):
    instrutores = Instrutor.objects.all()
    return render(request, 'instrutores/lista.html', {'instrutores': instrutores})

def detalhe_instrutor(request, pk):
    instrutor = get_object_or_404(Instrutor, pk=pk)
    return render(request, 'instrutores/detalhe.html', {'instrutor': instrutor})

def criar_instrutor(request):
    if request.method == 'POST':
        form = InstrutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_instrutores')
    else:
        form = InstrutorForm()
    return render(request, 'instrutores/form.html', {'form': form})

def editar_instrutor(request, pk):
    instrutor = get_object_or_404(Instrutor, pk=pk)
    if request.method == 'POST':
        form = InstrutorForm(request.POST, instance=instrutor)
        if form.is_valid():
            form.save()
            return redirect('lista_instrutores')
    else:
        form = InstrutorForm(instance=instrutor)
    return render(request, 'instrutores/form.html', {'form': form})

def excluir_instrutor(request, pk):
    instrutor = get_object_or_404(Instrutor, pk=pk)
    if request.method == 'POST':
        instrutor.delete()
        return redirect('lista_instrutores')
    return render(request, 'instrutores/exclusao.html', {'instrutor': instrutor})
