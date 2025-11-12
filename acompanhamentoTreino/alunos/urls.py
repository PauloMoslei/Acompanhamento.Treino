from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('<int:aluno_id>/', views.detalhe_aluno, name='detalhe_aluno'),
    path('minha/ficha/', views.minha_ficha, name='minha_ficha'),
]
