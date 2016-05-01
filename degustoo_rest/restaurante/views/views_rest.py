from django.http import Http404

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
#from rest_framework.response import Response

from restaurante.serializers import *
from restaurante.permissions import *
from restaurante.models import *

class RestauranteRest(viewsets.ModelViewSet):
	queryset = Restaurante.objects.all()
	serializer_class = RestauranteSerializer

class CardapioRest(viewsets.ModelViewSet):
	permission_classes = (MenuOwnerOrReadyOnly,)
	serializer_class = CardapioSerializer

	def get_queryset(self):
		try:
			restaurante = Restaurante.objects.get(pk=self.r_pk)
			return restaurante.getEvery_menu()
		except:
			raise Http404

	def dispatch(self, request, *args, **kwargs):
		self.r_pk = kwargs.pop('r_pk',0)
		return super(CardapioRest, self).dispatch(request, *args, **kwargs)

class OpcaoRest(viewsets.ModelViewSet):
	permission_classes = (OptionOwnerOrReadyOnly,)
	serializer_class = OpcaoSerializer

	def get_queryset(self):
		try:
			cardapio = Cardapio.objects.get(pk=self.c_pk)
			return cardapio.getEvery_option()
		except:
			raise Http404

	def dispatch(self, request, *args, **kwargs):
		self.c_pk = kwargs.pop('c_pk',0)
		return super(OpcaoRest, self).dispatch(request, *args, **kwargs)

class SubcardapioRest(viewsets.ModelViewSet):
	permission_classes = (SubmenuOwnerOrReadyOnly,)
	serializer_class = SubcardapioSerializer

	def get_queryset(self):
		try:
			cardapio = Cardapio.objects.get(pk=self.c_pk)
			return cardapio.getEvery_submenu()
		except:
			raise Http404

	def dispatch(self, request, *args, **kwargs):
		self.c_pk = kwargs.pop('c_pk',0)
		return super(SubcardapioRest, self).dispatch(request, *args, **kwargs)

class ItemCardapioRest(viewsets.ModelViewSet):
	permission_classes = (ItemOwnerOrReadyOnly,)
	serializer_class = ItemSerializer

	def get_queryset(self):
		try:
			cardapio = Cardapio.objects.get(pk=self.c_pk)
			return cardapio.getEvery_item()
		except:
			raise Http404

	def dispatch(self, request, *args, **kwargs):
		self.c_pk = kwargs.pop('c_pk',0)
		return super(ItemCardapioRest, self).dispatch(request, *args, **kwargs)

class ItemSubcardapioRest(viewsets.ModelViewSet):
	permission_classes = (ItemOwnerOrReadyOnly,)
	serializer_class = ItemSerializer

	def get_queryset(self):
		try:
			subcardapio = Cardapio.objects.get(pk=self.s_pk)
			return subcardapio.getEvery_item()
		except:
			raise Http404

	def dispatch(self, request, *args, **kwargs):
		self.s_pk = kwargs.pop('s_pk',0)
		return super(ItemSubcardapioRest, self).dispatch(request, *args, **kwargs)

class ItemOpcaoRest(viewsets.ModelViewSet):
	permission_classes = (ItemOwnerOrReadyOnly,)
	serializer_class = ItemSerializer

	def get_queryset(self):
		try:
			opcao = Opcao.objects.get(pk=self.o_pk)
			return opcao.getEvery_item()
		except:
			raise Http404

	def dispatch(self, request, *args, **kwargs):
		self.o_pk = kwargs.pop('o_pk',0)
		return super(ItemOpcaoRest, self).dispatch(request, *args, **kwargs)