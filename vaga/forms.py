from django import forms
from .models import VagaEmprego

class VagaEmpregoForm(forms.ModelForm):
    class Meta:
        model = VagaEmprego
        fields = ['descricao', 'foto', 'telefone_contato', 'ativo']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'telefone_contato': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }