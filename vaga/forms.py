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

class VagaFiltroForm(forms.Form):
    """Formulário para filtrar vagas"""
    
    descricao = forms.CharField(required=False, label='Descrição')
    data_inicio = forms.DateField(required=False, label='Data Início')
    data_fim = forms.DateField(required=False, label='Data Fim')
    apenas_ativas = forms.BooleanField(required=False, label='Apenas vagas ativas')
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['descricao'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Buscar por descrição...'
        })
        
        self.fields['data_inicio'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })
        
        self.fields['data_fim'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })
        
        self.fields['apenas_ativas'].widget.attrs.update({
            'class': 'form-check-input'
        })