from django import forms

from core.models import Usuario
from django.forms import ModelForm

class Form_Registro(ModelForm):

    class Meta:
        model = Usuario
        fields = ['email', 'telefone']
        widgets = {
            "email": forms.EmailInput(attrs={"class":'form-control'}),
            "telefone": forms.TextInput(attrs={'class':'form-control'})
        }
    
    def clean_senha2(self):
        pass1 = self.cleaned_data['senha1']
        pass2 = self.cleaned_data['senha2']
        
        if (pass1 and pass2) and (pass1 == pass2):
            return pass2
        else:
            raise forms.ValidationError("Passwords do not match")

class Form_Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    
    class Meta:
        labels = {
            "password": "Senha"
        }
        widgets = {
           "email": forms.EmailInput(attrs={'class':'form-control'}),
           "password": forms.PasswordInput(attrs={'class':'form-control'})
        }