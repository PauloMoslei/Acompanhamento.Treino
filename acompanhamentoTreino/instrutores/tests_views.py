from django.test import TestCase
from django.urls import reverse
from .models import Instrutor

class InstrutorViewsTest(TestCase):

    def setUp(self):
        self.instrutor = Instrutor.objects.create(
            nome="Carlos Silva",
            especialidade="Musculação",
            telefone="(11) 99999-1111",
            email="carlos@example.com",
            observacoes="Instrutor certificado"
        )

    def test_lista_instrutores_view(self):
        """Testa se a view de lista retorna status 200 e usa o template correto."""
        url = reverse('lista_instrutores')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instrutores/lista.html')
        self.assertContains(response, self.instrutor.nome)

    def test_detalhe_instrutor_view(self):
        """Testa a view de detalhe de um instrutor."""
        url = reverse('detalhe_instrutor', args=[self.instrutor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instrutores/detalhe.html')
        self.assertContains(response, self.instrutor.nome)

    def test_criar_instrutor_view(self):
        """Testa a criação de um novo instrutor via POST."""
        url = reverse('criar_instrutor')
        data = {
            'nome': 'Ana Souza',
            'especialidade': 'Funcional',
            'telefone': '(11) 98888-2222',
            'email': 'ana@example.com',
            'observacoes': 'Nova instrutora'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Instrutor.objects.filter(nome='Ana Souza').exists())

    def test_editar_instrutor_view(self):
        """Testa a edição de um instrutor existente via POST."""
        url = reverse('editar_instrutor', args=[self.instrutor.pk])
        data = {
            'nome': 'Carlos Silva Editado',
            'especialidade': 'Pilates',
            'telefone': '(11) 97777-3333',
            'email': 'carlos_edit@example.com',
            'observacoes': 'Alterado'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.instrutor.refresh_from_db()
        self.assertEqual(self.instrutor.nome, 'Carlos Silva Editado')
        self.assertEqual(self.instrutor.especialidade, 'Pilates')

    def test_excluir_instrutor_view(self):
        """Testa a exclusão de um instrutor via POST."""
        url = reverse('excluir_instrutor', args=[self.instrutor.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Instrutor.objects.filter(pk=self.instrutor.pk).exists())
