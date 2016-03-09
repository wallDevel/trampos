from django import forms

class Form_Avaliavel_Register(forms.Form):
	CHOICE = (
		('2', 'AVALIAVEL'),
		('3', 'VINI PORCA ROSA'),
	)

	email = forms.EmailField()
	telefone = forms.CharField(max_length=50)
	password1 = forms.CharField(max_length=16)
	password2 = forms.CharField(max_length=16)
	nivel = forms.ChoiceField(choices=CHOICE)

	cnpj = forms.CharField(max_length=50)
	razao_social = forms.CharField(max_length=100)
	nome_fantasia = forms.CharField(max_length=100)
	email_institucional = forms.EmailField()

	nome_responsavel = forms.CharField(max_length=100)
	email_responsavel = forms.EmailField()
	cpf_responsavel = forms.CharField(max_length=50)
	telefone_responsavel = forms.CharField(max_length=50)

class Form_Avaliavel_Register_Beta(forms.Form):
	

	SS = (
		('Culinario', 
			(
				('restaurante','restaurante'),('pizzaria','pizzaria'),('lanchonete', 'lanchonete')
			)
		),
	)

	nome = forms.CharField(max_length=50)
	telefone = forms.CharField(max_length=50)
	setor = forms.ChoiceField(choices=SS)
	subsetor = forms.ChoiceField(choices=SS)

	estado = forms.CharField(max_length=50)
	municipio = forms.CharField(max_length=50)
	bairro = forms.CharField(max_length=50)
	rua = forms.CharField(max_length=50)
	numero = forms.CharField(max_length=50)

class Form_Search_Test(forms.Form):
	nome = forms.CharField(max_length=100)