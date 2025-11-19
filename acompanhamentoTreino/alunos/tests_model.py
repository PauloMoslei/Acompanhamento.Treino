from django.test import TestCase
from .models import Aluno

class AlunoModelTest(TestCase):

    def setUp(self):
        self.aluno = Aluno.objects.create(
            nome="João Silva",
            idade=28,
            objetivo="Hipertrofia",
            telefone="(11) 99999-1111",
            email="joao@example.com"
        )

    def test_aluno_criacao(self):
        self.assertIsInstance(self.aluno, Aluno)
        self.assertEqual(self.aluno.nome, "João Silva")
        self.assertEqual(self.aluno.idade, 28)
        self.assertEqual(self.aluno.objetivo, "Hipertrofia")

    def test_aluno_str(self):
        self.assertEqual(str(self.aluno), "João Silva")

    def test_campos_opcionais(self):
        aluno2 = Aluno.objects.create(nome="Maria Santos", idade=32)
        self.assertIsNone(aluno2.objetivo)
        self.assertIsNone(aluno2.telefone)
        self.assertIsNone(aluno2.email)
