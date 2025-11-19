from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'objetivo', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do aluno'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}),
            'objetivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Hipertrofia, Emagrecimento'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
        }
