from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from django.http import Http404, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from forms import *
from core.models import Usuario, Endereco
from restaurante.models import Restaurante

class Index(View):
	template = "administracao/index.html"
	def get(self, request):
		return render(request, self.template, {})

class Registrar_Restaurante(View):
	template = "administracao/registrar_restaurante.html"
	form_class = Form_Restaurante_Novo
	
	def get(self, request):
		form = self.form_class()
		return render(request, self.template, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email'] 
			password = form.cleaned_data['password2']
			telefone = form.cleaned_data['telefone']
			nivel = form.cleaned_data['nivel']

			usuario = Usuario.objects.create_user(email=email,password=password,nivel=nivel,telefone=telefone)

			estado = form.cleaned_data['estado']
			municipio = form.cleaned_data['municipio']
			bairro = form.cleaned_data['bairro']
			rua = form.cleaned_data['rua']
			numero = form.cleaned_data['numero']
			complemento = form.cleaned_data['complemento']
			cep = form.cleaned_data['cep']

			endereco = Endereco(estado=estado,municipio=municipio,bairro=bairro,rua=rua,
				numero=numero,complemento=complemento,cep=cep)
			endereco.save()

			nome = form.cleaned_data['nome']
			cnpj = form.cleaned_data['cnpj']

			restaurante = Restaurante(usuario=usuario,endereco=endereco,nome=nome,cnpj=cnpj)
			restaurante.save()
		return render(request, self.template, {'form': form})