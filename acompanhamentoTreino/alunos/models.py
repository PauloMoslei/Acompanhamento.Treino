from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    objetivo = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
