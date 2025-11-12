from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    """
    Representa um aluno da academia.
    Cada aluno está vinculado a um usuário do sistema (User).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
