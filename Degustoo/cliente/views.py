from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import Http404, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from .models import *
#from .forms import *

class Index(View):
	template = 'cliente/index.html'
	def get(self, request):
		return render(request, self.template, {})