from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from django.http import Http404, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from degAuth.models import Usuario
from core.models import Endereco
from restaurante.models import Restaurante, GerenciadorRestaurante

from .forms import *
from index.forms import *

class AdminMixin(object):
	admin = None
	def dispatch(self, request, *args, **kwargs):
		try:
			user = request.user
			if user.is_staff:
				self.admin = user
			else:
				raise Http404("User has not permission to visit this page")
		except Exception:
			raise Http404("User has not permission to visit this page")
		return super(AdminMixin, self).dispatch(request, *args, **kwargs)

class Index(AdminMixin, View):
	template = "administracao/index.html"
	def get(self, request):
		return render(request, self.template, {})

class Registrar_Restaurante(AdminMixin, View):
	template = "administracao/registrar_restaurante.html"
	form_class = Form_Restaurant_Register
	
	def get(self, request):
		form = self.form_class()
		return render(request, self.template, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			nome_responsavel = form.cleaned_data['nome_completo_responsavel']
			email_responsavel = form.cleaned_data['email_responsavel']
			tel_responsavel = form.cleaned_data['telefone_responsavel']
			cpf = form.cleaned_data['cpf_responsavel']

			responsavel = GerenciadorRestaurante(email=email_responsavel,telefone=tel_responsavel,nome_completo=nome_responsavel,cpf=cpf)
			responsavel.save()

			email = form.cleaned_data['email'] 
			password = form.cleaned_data['password2']
			telefone = form.cleaned_data['telefone']

			usuario = Usuario.objects.create_restaurant_user(email=email,password=password,telefone=telefone)

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
			nivel = form.cleaned_data['nivel']

			restaurante = Restaurante(usuario=usuario,gerenciador=responsavel,endereco=endereco,nome=nome,cnpj=cnpj,tipo=nivel)
			restaurante.save()
		return render(request, self.template, {'form': form})