from django.test import TestCase
from django.urls import reverse
from .models import Aluno

class AlunoViewsTest(TestCase):

    def setUp(self):
        self.aluno = Aluno.objects.create(nome="João Silva", idade=28, objetivo="Hipertrofia")

    def test_lista_alunos_view(self):
        url = reverse('lista_alunos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alunos/lista.html')
        self.assertContains(response, self.aluno.nome)

    def test_detalhe_aluno_view(self):
        url = reverse('detalhe_aluno', args=[self.aluno.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alunos/detalhe.html')
        self.assertContains(response, self.aluno.nome)

    def test_criar_aluno_view(self):
        url = reverse('criar_aluno')
        data = {'nome': 'Maria Santos', 'idade': 32, 'objetivo': 'Emagrecimento'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Aluno.objects.filter(nome='Maria Santos').exists())

    def test_editar_aluno_view(self):
        url = reverse('editar_aluno', args=[self.aluno.pk])
        data = {'nome': 'João Silva Editado', 'idade': 29, 'objetivo': 'Condicionamento'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.nome, 'João Silva Editado')
        self.assertEqual(self.aluno.idade, 29)

    def test_excluir_aluno_view(self):
        url = reverse('excluir_aluno', args=[self.aluno.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Aluno.objects.filter(pk=self.aluno.pk).exists())
