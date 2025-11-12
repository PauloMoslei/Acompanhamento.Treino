from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from alunos.models import Aluno
from fichas.models import FichaTreino # type: ignore

class AlunoViewsTest(TestCase):

    def setUp(self):
        # Criação de um usuário instrutor (staff)
        self.instrutor = User.objects.create_user(
            username='instrutor',
            password='123456',
            is_staff=True
        )

        # Criação de um usuário aluno
        self.user_aluno = User.objects.create_user(
            username='aluno1',
            password='123456'
        )

        # Criação do registro do aluno
        self.aluno = Aluno.objects.create(
            user=self.user_aluno,
            nome='Aluno Teste'
        )

        # Criação de uma ficha de treino para o aluno
        self.ficha = FichaTreino.objects.create(
            aluno=self.aluno,
            nome='Treino A'
        )

    def test_lista_alunos_acesso_instrutor(self):
        """Instrutor deve conseguir acessar a lista de alunos."""
        self.client.login(username='instrutor', password='123456')
        response = self.client.get(reverse('alunos:lista_alunos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alunos/lista_alunos.html')
        self.assertContains(response, 'Aluno Teste')

    def test_lista_alunos_acesso_aluno_negado(self):
        """Aluno comum não deve acessar a lista de alunos."""
        self.client.login(username='aluno1', password='123456')
        response = self.client.get(reverse('alunos:lista_alunos'))
        self.assertTemplateUsed(response, 'acesso_negado.html')

    def test_detalhe_aluno_instrutor_ok(self):
        """Instrutor pode acessar o detalhe de qualquer aluno."""
        self.client.login(username='instrutor', password='123456')
        response = self.client.get(reverse('alunos:detalhe_aluno', args=[self.aluno.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Treino A')

    def test_detalhe_aluno_acesso_proprio_ok(self):
        """Aluno pode acessar apenas o próprio detalhe."""
        self.client.login(username='aluno1', password='123456')
        response = self.client.get(reverse('alunos:detalhe_aluno', args=[self.aluno.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Treino A')

    def test_detalhe_aluno_acesso_negado_outro_aluno(self):
        """Aluno não pode acessar a ficha de outro aluno."""
        outro_user = User.objects.create_user(username='aluno2', password='123456')
        outro_aluno = Aluno.objects.create(user=outro_user, nome='Outro Aluno')

        self.client.login(username='aluno1', password='123456')
        response = self.client.get(reverse('alunos:detalhe_aluno', args=[outro_aluno.id]))
        self.assertTemplateUsed(response, 'acesso_negado.html')

    def test_minha_ficha_aluno_ok(self):
        """Aluno deve conseguir ver sua própria ficha."""
        self.client.login(username='aluno1', password='123456')
        response = self.client.get(reverse('alunos:minha_ficha'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Treino A')
