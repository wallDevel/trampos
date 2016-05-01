from django.shortcuts import render

# Create your views here.
from core.ajax.response import *

from django.views.generic import View
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from restaurante.models import *
from restaurante.forms import *
from restaurante.tables import *
from .mixins import *

class SubcardapioView(RestauranteMixin, CardapioMixin, SubcardapioMixin, View):
    """
        View de pagina de subcardapio onde o usuario pode adicionar/editar/deletar itens
        de determinado subcardapio
    """
    template = 'restaurante/cardapio/subcardapio.html'
    def get(self, request):
        itens = self.subcardapio.getEvery_item()
        return render(request, self.template, {'cardapio':self.cardapio, 'subcardapio':self.subcardapio, 'itens':itens})

class CriarSubcardapio(RestauranteMixin, CardapioMixin, View):
    """
        Cria subcardapio via json
    """
    form_class = Form_Subcardapio_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            if self.cardapio.submenuTitleIsFree(form.cleaned_data['titulo']):
                subcardapio = Subcardapio(cardapio = self.cardapio, titulo=form.cleaned_data['titulo'])
                subcardapio.save()

                # prepare data to send back using json
                subcardapios = self.cardapio.getEvery_submenu()
                result = buildSubcardapioTable(subcardapios, self.cardapio.id, token=request.COOKIES['csrftoken'])
                data = prepareAjaxSuccessData(result, len(subcardapios))
            else:
                # there is an object with the same name in the same menu
                data = prepareAjaxErrorMessage('A submenu with the same name was found')
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class EditarSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, View):
    """
        Edita subcardapio via json
    """
    template = 'restaurante/cardapio/editar_subcardapio.html'
    form_class = Form_Subcardapio_Default
    def get(self, request):
        form = self.form_class(instance=self.subcardapio)
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST, instance=self.subcardapio)
        if form.is_valid():
            form.save()
            subcardapios = self.cardapio.getEvery_submenu()
            result = buildSubcardapioTable(subcardapios, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(subcardapios))
        return JsonResponse(data)

class DeletarSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, View):
    """
        Deleta subcardapio via json
    """
    form_class = Form_Subcardapio_Delete
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            subcardapio = Subcardapio.objects.get(pk=form.cleaned_data['id'])
            subcardapio.delete()
            subcardapios = self.cardapio.getEvery_submenu()
            result = buildSubcardapioTable(subcardapios, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success':1, 'result':result}
        return JsonResponse(data)


class CriarItemSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, View):
    """
        Cria item de subcardapio via json
    """
    form_class = Form_Item_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            if self.subcardapio.itemNameIsFree(form.cleaned_data['nome']):
                item = Item(
                    sub_cardapio = self.subcardapio, nome=form.cleaned_data['nome'],
                    preco=form.cleaned_data['preco'],ingredientes=form.cleaned_data['ingredientes'])
                item.save()

                # prepare data to send back using json
                itens = self.subcardapio.getEvery_item()
                result = buildItemSubcardapioTable(itens, self.cardapio.id, self.subcardapio.id, token=request.COOKIES['csrftoken'])
                
                data = prepareAjaxSuccessData(result, len(itens))
            else:
                # there is an object with the same name in the same menu
                data = prepareAjaxErrorMessage('Item with this name already exists in this submenu')
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class EditarItemSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, ItemSubcardapioMixin, View):
    """
        Edita item de subcardapio via json
    """

    form_class = Form_Item_Default

    def post(self, request):
        form = self.form_class(request.POST, instance=self.item)
        if form.is_valid():
            form.save()
            itens = self.subcardapio.getEvery_item()
            result = buildItemSubcardapioTable(itens, self.cardapio.id, self.subcardapio.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        return JsonResponse(data)

class DeletarItemSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, ItemSubcardapioMixin, View):
    """
        Deleta item de subcardapio via json
    """

    form_class = Form_Item_Delete

    def post(self, request):
        form = self.form_class(request.POST) 
        if form.is_valid():
            item = Item.objects.get(pk=form.cleaned_data['id'])
            item.delete()
            itens = self.subcardapio.getEvery_item()
            result = buildItemSubcardapioTable(itens, self.cardapio.id, self.subcardapio.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        return JsonResponse(data)