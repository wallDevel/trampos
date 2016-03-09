from django import forms
from django.forms import ModelForm

from django.utils.translation import ugettext_lazy as _

from .models import *

#################
#### CARDAPIO FORM
#################
class Form_Cardapio_Default(ModelForm):
    imagem = forms.ImageField(required=False)
    class Meta:
        model = Cardapio
        fields = ['titulo', 'tipo', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
        }

#################
#### SUBCARDAPIO FORM
#################
class Form_Subcardapio_Default(ModelForm):
    class Meta:
        model = Subcardapio
        fields = ['titulo']
        widgets = {
            "titulo": forms.TextInput(attrs={'class':'form-control'})
        }

class Form_Subcardapio_Delete(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)

#################
#### OPCAO FORM
#################
class Form_Opcao_Default(ModelForm):
    class Meta:
        model = Opcao
        fields = ['rotulo']
        widgets = {
           'rotulo': forms.TextInput(attrs={'class':'form-control'})
        }

class Form_Opcao_Delete(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)

class Form_Opcao_Import(forms.Form):
    options = forms.ModelMultipleChoiceField(
        queryset=Cardapio.objects.none(), 
        label="Importar itens")
    
    def __init__(self, *args, **kwargs):
        cardapio = kwargs.pop('cardapio', None)
        super(Form_Opcao_Import, self).__init__(*args, **kwargs)
        self.fields['options'].queryset = cardapio.opcao_set.all()
        

#################
#### ITEM FORM
#################
class Form_Item_Default(ModelForm):
    preco = forms.DecimalField(max_digits=4, decimal_places=2, localize=True)
    
    def __init__(self, *args, **kargs):
        cardapio = kargs.pop('cardapio', None)

        super(Form_Item_Default, self).__init__(*args, **kargs)

        if cardapio:
            self.fields['grandezas_variaveis'].queryset = cardapio.grandezavariavel_set.all()

    class Meta:
        model = Item
        fields = ('nome', 'preco', 'ingredientes')
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'preco': forms.TextInput(attrs={'class':'form-control'}),
            'ingredientes': forms.TextInput(attrs={'class':'form-control'}),
        }

class Form_Item_Delete(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)