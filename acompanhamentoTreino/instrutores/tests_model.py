from django.test import TestCase
from .models import Instrutor

class InstrutorModelTest(TestCase):

    def setUp(self):
        self.instrutor = Instrutor.objects.create(
            nome="Carlos Silva",
            especialidade="Musculação",
            telefone="(11) 99999-1111",
            email="carlos@example.com",
            observacoes="Instrutor certificado em musculação avançada"
        )

    def test_instrutor_criacao(self):
        """Testa se o instrutor foi criado corretamente."""
        self.assertIsInstance(self.instrutor, Instrutor)
        self.assertEqual(self.instrutor.nome, "Carlos Silva")
        self.assertEqual(self.instrutor.especialidade, "Musculação")
        self.assertEqual(self.instrutor.telefone, "(11) 99999-1111")
        self.assertEqual(self.instrutor.email, "carlos@example.com")
        self.assertEqual(self.instrutor.observacoes, "Instrutor certificado em musculação avançada")

    def test_instrutor_str(self):
        """Testa o método __str__ do modelo."""
        self.assertEqual(str(self.instrutor), "Carlos Silva")

    def test_instrutor_campos_opcionais(self):
        """Testa criação de instrutor sem campos opcionais."""
        instrutor2 = Instrutor.objects.create(nome="Ana Souza")
        self.assertEqual(instrutor2.nome, "Ana Souza")
        self.assertIsNone(instrutor2.especialidade)
        self.assertIsNone(instrutor2.telefone)
        self.assertIsNone(instrutor2.email)
        self.assertIsNone(instrutor2.observacoes)
