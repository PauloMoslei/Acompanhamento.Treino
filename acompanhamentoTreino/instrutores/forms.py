from django import forms
from .models import Instrutor

class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome', 'especialidade', 'telefone', 'email', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do instrutor'
            }),
            'especialidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Musculação, Pilates, Funcional'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(99) 99999-9999'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Observações adicionais'
            }),
        }
