from django.views.generic import View
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

class RestauranteMixin(object):
    """ 
        Verify if there are some restaurant logged in and raises an error if not 
    """
    restaurante = None
    "Verify if there is some restaurant logged in"
    def dispatch(self, request, *args, **kwargs):
        try:
            user = request.user
            if user.is_restaurant:
                self.user = user
                self.restaurante = user.restaurante
        except Exception:
            raise Http404("You are not allowed visiting here")
        return super(RestauranteMixin, self).dispatch(request, *args, **kwargs)

class CardapioMixin(object):
    """
        Verify if there are some the given menu.pk belows to this user
    """
    cardapio = None
    def dispatch(self, request, *args, **kwargs):
        id = kwargs.pop('card_id', 0)
        if not id == 0:
            try:
                restaurante = self.restaurante
                self.cardapio = restaurante.cardapio_set.get(pk=id)
            except Cardapio.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(CardapioMixin, self).dispatch(request, *args, **kwargs)

class SubcardapioMixin(object):
    """
        Ao carregar a view verifica se o subcardapio pertence a este cardapio.
        Se sim, aplica a variavel "subcardapio" ao objeto view
    """
    subcardapio = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('id', 0)
        if id:
            try:
                self.subcardapio = self.cardapio.subcardapio_set.get(pk=id)
            except Subcardapio.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(SubcardapioMixin, self).dispatch(request, **kwargs)


class OpcaoMixin(object):
    """
        Ao carregar a view verifica se a opcao pertence a este cardapio.
        Se sim, aplica a variavel "opcao" ao objeto view
    """
    opcao = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('id', 0)
        if id:
            try:
                self.opcao = self.cardapio.opcao_set.get(pk=id)
            except Opcao.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(OpcaoMixin, self).dispatch(request, **kwargs)

class ItemCardapioMixin(object):
    """
        Ao carregar a view verifica se o item pertence a este cardapio.
        Se sim, aplica a variavel "item" ao objeto view
    """
    item = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('i_id', 0)
        if id:
            try:
                self.item = self.cardapio.item_set.get(pk=id)
            except Item.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(ItemCardapioMixin, self).dispatch(request, **kwargs)

class ItemSubcardapioMixin(object):
    """
        Ao carregar a view verifica se o item pertence a este subcardapio.
        Se sim, aplica a variavel "item" ao objeto view
    """
    item = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('i_id', 0)
        if id:
            try:
                self.item = self.subcardapio.item_set.get(pk=id)
            except Item.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(ItemSubcardapioMixin, self).dispatch(request, **kwargs)

class ItemOpcaoMixin(object):
    """
        Ao carregar a view verifica se o item pertence a esta opcao.
        Se sim, aplica a variavel "item" ao objeto view
    """
    item = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('i_id', 0)
        if id:
            try:
                self.item = self.opcao.item_set.get(pk=id)
            except Item.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(ItemOpcaoMixin, self).dispatch(request, **kwargs)