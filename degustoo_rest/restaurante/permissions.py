from rest_framework import permissions

from restaurante.models import *

class RestaurantOwnerOrReadyOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return request.user.restaurante == obj

class MenuOwnerOrReadyOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return request.user.restaurante.cardapio_set.filter(pk=obj.pk).exists()

class OptionOwnerOrReadyOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		card = obj.cardapio
		return request.user.restaurante.cardapio_set.filter(pk=card.pk).exists()
		#return request.user.restaurante.opcao_set.filter(pk=obj.pk).exists()

class SubmenuOwnerOrReadyOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		card = obj.cardapio
		return request.user.restaurante.cardapio_set.filter(pk=card.pk).exists()
		#return request.user.restaurante.subcardapio_set.filter(pk=obj.pk).exists()

class ItemOwnerOrReadyOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		if obj.cardapio:
			cardapio = obj.cardapio
			return request.user.restaurante.cardapio_set.filter(pk=cardapio.pk).exists()
		elif obj.opcao:
			cardapio = obj.opcao.cardapio
			return request.user.restaurante.cardapio_set.filter(pk=cardapio.pk).exists()
		elif obj.sub_cardapio:
			cardapio = obj.sub_cardapio.cardapio
			return request.user.restaurante.cardapio_set.filter(pk=cardapio.pk).exists()
		else:
			return False