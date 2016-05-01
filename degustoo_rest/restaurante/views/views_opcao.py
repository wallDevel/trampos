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

class OpcaoView(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    """
        View de pagina de opcao onde o usuario pode adicionar/editar/deletar itens
        de determinada opcao
    """
    template = 'restaurante/cardapio/opcao.html'
    form_class = Form_Opcao_Import
    form_item_price = Form_Item_Price_Generator
    def get(self, request):
        form = self.form_class(cardapio=self.cardapio)
        form_item_price = self.form_item_price()
        itens = self.opcao.getEvery_item()
        return render(request, self.template, {'cardapio':self.cardapio, 'opcao':self.opcao, 'itens':itens, 'form':form, 'form_item_price': form_item_price})

    def post(self, request):
        form = self.form_class(request.POST, cardapio=self.cardapio)
        if form.is_valid():
            chosenOptions = form.cleaned_data['options']
            for option in chosenOptions:
                itens = option.exportItens()
                self.opcao.importItens(itens)
            result = buildItemOpcaoTable(self.opcao.item_set.all(), self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class CriarOpcao(RestauranteMixin, CardapioMixin, View):
    """
        Cria opcao via json
    """
    form_class = Form_Opcao_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if self.cardapio.optionLabelIsFree(form.cleaned_data['rotulo']):
                opcao = Opcao(cardapio = self.cardapio, rotulo=form.cleaned_data['rotulo'])
                opcao.save()
                # prepare data to send back using json
                opcoes = self.cardapio.getEvery_option()
                result = buildOpcaoTable(opcoes, self.cardapio.id, token=request.COOKIES['csrftoken'])
                data = prepareAjaxSuccessData(result, len(opcoes))
            else:
                # there is an object with the same name in the same menu
                data = prepareAjaxErrorMessage('Option with this name already exists')
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class EditarOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    """
        Edita opcao via json
    """
    template = 'restaurante/cardapio/editar_opcao.html'
    form_class = Form_Opcao_Default
    def get(self, request):
        form = self.form_class(instance=self.opcao)
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST, instance=self.opcao)
        if form.is_valid():
            form.save()
            opcoes = self.cardapio.getEvery_option()
            result = buildOpcaoTable(opcoes, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(opcoes))
        return JsonResponse(data)

class DeletarOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    """
        Deleta opcao via json
    """
    form_class = Form_Item_Delete
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            opcao = Opcao.objects.get(pk=form.cleaned_data['id'])
            opcao.delete()
            opcoes = self.cardapio.getEvery_option()
            result = buildOpcaoTable(opcoes, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(opcoes))
        return JsonResponse(data)


class CriarItemOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    """
        Cria item de opcao via json
    """
    form_class = Form_Item_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            if self.opcao.itemNameIsFree(form.cleaned_data['nome']):
                item = Item(
                    opcao = self.opcao, nome=form.cleaned_data['nome'],
                    preco=form.cleaned_data['preco'],ingredientes=form.cleaned_data['ingredientes'])
                item.save()
                # prepare data to send back using json
                itens = self.opcao.getEvery_item()
                result = buildItemOpcaoTable(itens, self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
                
                data = prepareAjaxSuccessData(result, len(itens))
            else:
                # there is an object with the same name in the same menu
                data = prepareAjaxErrorMessage('Item with this name already exists in this option')
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class EditarItemOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, ItemOpcaoMixin, View):
    """
        Edita item de opcao via json
    """

    form_class = Form_Item_Default

    def post(self, request):
        form = self.form_class(request.POST, instance=self.item)
        if form.is_valid():
            form.save()
            itens = self.opcao.getEvery_item()
            result = buildItemOpcaoTable(itens, self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        return JsonResponse(data)

class ItemOpcaoGenerator(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    form_class = None
    def post(self, request):
        form = self.form_class
        if form.is_valid():
            self.opcao.setEvery_item_price(form.cleaned_data[''])
            itens = self.opcao.getEvery_item()
            result = buildItemOpcaoTable(itens, self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        return JsonResponse(data)

class ItemPriceGenerator(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    # Gera preço para todos os itens de determinada opção
    form_class = Form_Item_Price_Generator
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.opcao.setEvery_item_price(form.cleaned_data['preco'])
            itens = self.opcao.getEvery_item()
            result = buildItemOpcaoTable(itens, self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        else:
            data = prepareAjaxErrorMessage('Erro ao tentar salvar itens. Formulário não é válido.')
        return JsonResponse(data)

class DeletarItemOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, ItemOpcaoMixin, View):
    """
        Deleta item de cardapio via json
    """
    form_class = Form_Item_Delete

    def post(self, request):
        form = self.form_class(request.POST) 
        if form.is_valid():
            item = Item.objects.get(pk=form.cleaned_data['id'])
            item.delete()
            itens = self.opcao.getEvery_item()
            result = buildItemOpcaoTable(itens, self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        return JsonResponse(data)