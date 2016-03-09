from django.shortcuts import render

# Create your views here.
from django.views.generic import View

# My imports
from forms import *
from avaliavel.models import *
from core.models import *

class RegistrarAvaliavel(View):
	template = "administrador/registro_avaliavel.html"
	form_class = Form_Avaliavel_Register_Beta
	def get(self, request):
		form = self.form_class()
		return render(request, self.template, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			estado = form.cleaned_data['estado']
			municipio = form.cleaned_data['municipio']
			bairro = form.cleaned_data['bairro']
			rua = form.cleaned_data['rua']
			numero = form.cleaned_data['numero']
			
			endereco = Endereco_Beta(estado=estado,municipio=municipio,bairro=bairro,rua=rua,numero=numero)
			endereco.save()

			telefone = form.cleaned_data['telefone']
			nome = form.cleaned_data['nome']
			setor = form.cleaned_data['setor']
			subsetor = form.cleaned_data['subsetor']
			avaliavel = Avaliavel_Beta(telefone=telefone,nome=nome,setor=setor,subsetor=subsetor,endereco_beta=endereco)
			avaliavel.save()
		return render(request, self.template, {'form':form})


class PesquisarAvaliavel(View):
	template = "administrador/pesquisar_avaliavel.html"
	form_class = Form_Search_Test

	def get(self, request):
		form = self.form_class()
		return render(request, self.template, {'form':form})	

	def post(self, request):
		avaliaveis = None
		form = self.form_class(request.POST)
		if form.is_valid():
			nome = form.cleaned_data['nome']
			avaliaveis = Avaliavel_Beta.objects.filter(nome__istartswith=nome)
		return render(request, self.template, {'avaliaveis':avaliaveis, 'form':form})