from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista.html', {'alunos': alunos})

def detalhe_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'alunos/detalhe.html', {'aluno': aluno})

def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/form.html', {'form': form})

def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/form.html', {'form': form})

def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'alunos/exclusao.html', {'aluno': aluno})
