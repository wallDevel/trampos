from django.shortcuts import render

# Create your views here.
from core.ajax.response import *

from django.views.generic import View
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render#, render_to_response, get_object_or_404, redirect

from restaurante.models import *
from restaurante.forms import *
from restaurante.tables import *
from .mixins import *




class Index(RestauranteMixin, View):
    template = "restaurante/index.html"
    def get(self, request):
        return render(request, self.template)

class Promocoes(RestauranteMixin, View):
	template = "restaurante/promocoes.haml"
	def get(self, request):
		promocoes = self.restaurante.get_promocoes()
		return render(request, self.template, {'promocoes': promocoes})

	def post(self, request):
		pass

class Combos(RestauranteMixin, View):
	template = "restaurante/combos.haml"
	def get(self, request):
		combos = self.restaurante.get_combos()
		return render(request, self.template, {'combos': combos})
	
	def post(self, request):
		pass