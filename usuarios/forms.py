from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UsuarioAdaptado


class UsuarioAdaptadoCreationForm(UserCreationForm):
    class Meta:
        model = UsuarioAdaptado
        fields = [
            'username', 'email', 'cpf', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro', 'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF (apenas números)'}),
            'nome_cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da mãe'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'nome_bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirme a senha'})



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nome de usuário' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Senha'}))