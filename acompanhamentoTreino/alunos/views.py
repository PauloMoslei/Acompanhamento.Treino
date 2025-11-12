from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Aluno
from fichas.models import FichaTreino # type: ignore

@login_required
def lista_alunos(request):
    """
    Exibe a lista de alunos (visão do instrutor).
    """
    if not request.user.is_staff:  # Apenas instrutores podem ver todos os alunos
        return render(request, 'acesso_negado.html')

    alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})


@login_required
def detalhe_aluno(request, aluno_id):
    """
    Exibe os detalhes de um aluno e suas fichas de treino.
    """
    aluno = get_object_or_404(Aluno, id=aluno_id)

    # Se o usuário logado for aluno, só pode ver sua própria ficha
    if not request.user.is_staff and aluno.user != request.user:
        return render(request, 'acesso_negado.html')

    fichas = FichaTreino.objects.filter(aluno=aluno)
    return render(request, 'alunos/detalhe_aluno.html', {
        'aluno': aluno,
        'fichas': fichas
    })


@login_required
def minha_ficha(request):
    """
    Exibe a ficha de treino do aluno logado.
    """
    aluno = get_object_or_404(Aluno, user=request.user)
    fichas = FichaTreino.objects.filter(aluno=aluno)

    return render(request, 'alunos/minha_ficha.html', {
        'aluno': aluno,
        'fichas': fichas
    })
