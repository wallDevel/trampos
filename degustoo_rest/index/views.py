from django.shortcuts import render


from django.views.generic import View
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import *

import json
import unicodedata

class Index(View):
    template = "index/hamlpy/index.haml"
    def get(self, request):
        return render(request, self.template, {})

class Registrar(View):
    template = "index/hamlpy/registrar.haml"
    form_class = Form_Registro
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
            # save user on database
        return render(request, self.template, {'form':form})

class RegistroRestaurante(View):
    template = "index/hamlpy/registrar_restaurante.haml"
    form_class = Form_Restaurant_Register

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # send email to Degustoo with the form data
            return render(request, self.template, {'form': form})
        else:
            erros = json.dumps(form.errors)
            data = json.dumps(dict([(k, [str(e) for e in v]) for k,v in form.errors.items()]))
            return HttpResponseBadRequest(data, content_type='application/json')
            
class Login(View):
    template = "index/hamlpy/login.haml"
    form_class = Form_Login
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            #log user in
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # redirect to the right page
                    if user.nivel == 0:
                        return redirect('administracao:index')
                    elif user.nivel == 1:
                        return redirect('cliente:index')
                    elif user.nivel == 2 or user.nivel == 3:
                        return redirect('restaurante:index')
                    else:
                        raise Http404("You are not a valid user")
                else:
                    raise Http404("You are not an active user, check your email account and send us an user confirmation")
        return render(request, self.template, {'form':form})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("index:index")