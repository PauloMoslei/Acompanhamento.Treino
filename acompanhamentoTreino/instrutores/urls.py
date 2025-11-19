from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_instrutores, name='lista_instrutores'),
    path('novo/', views.criar_instrutor, name='criar_instrutor'),
    path('<int:pk>/', views.detalhe_instrutor, name='detalhe_instrutor'),
    path('<int:pk>/editar/', views.editar_instrutor, name='editar_instrutor'),
    path('<int:pk>/excluir/', views.excluir_instrutor, name='excluir_instrutor'),
]
