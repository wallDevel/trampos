from django import forms
from django.forms import ModelForm

from core.models import Usuario

class Form_Restaurante_Novo(ModelForm):
	CHOICES = (
		(2, "Restaurante"),
		(3, "Restaurante Diamante")
	)
	nivel = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}))

	password1 = forms.CharField(min_length=6, max_length=16, widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Senha")
	password2 = forms.CharField(min_length=6, max_length=16, widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Confirmar senha")

	nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
	cnpj = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

	estado = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
	municipio = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
	bairro = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
	rua = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
	numero = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
	complemento = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
	cep = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Usuario
		fields = ('email', 'telefone')
		widgets = {
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'telefone': forms.TextInput(attrs={'class':'form-control'}),
		}
