from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import Http404, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from .models import *
#from .forms import *

class ClienteMixin(object):
	user = None
	def dispatch(self, request, *args, **kwargs):
		try:
			user = request.user
			if user.is_client:
				self.user = user
			else:
				raise Http404("User has not permission to visit this page")
		except Exception:
			raise Http404("User has not permission to visit this page")
		return super(AdminMixin, self).dispatch(request, *args, **kwargs)

class Index(ClienteMixin, View):
	template = 'cliente/index.html'
	def get(self, request):
		return render(request, self.template)