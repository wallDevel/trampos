from django.shortcuts import render


from django.views.generic import View
from django.http import Http404, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from forms import *

class Index(View):
    template = "index/index.html"
    def get(self, request):
        return render(request, self.template, {})

class Registrar(View):
    template = "index/registrar.html"
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

class Login(View):
    template = "index/login.html"
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