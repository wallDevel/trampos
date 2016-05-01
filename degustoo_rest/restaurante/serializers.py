from rest_framework import serializers

from restaurante import models

class RestauranteSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Restaurante
		fields = ('id', 'nome', 'cnpj', 'imagem', 'tipo',)
		read_only_fields = ('id',)

class CardapioSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Cardapio
		fields = ('id', 'restaurante', 'imagem', 'titulo', 'tipo',)
		read_only_fields = ('id',)

class OpcaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Opcao
		fields = ('id', 'cardapio', 'rotulo',)
		read_only_fields = ('id',)

class SubcardapioSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Subcardapio
		fields = ('id', 'cardapio', 'titulo',)
		read_only_fields = ('id',)

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Item
		fields = ('id', 'nome', 'preco', 'ingredientes', 'cardapio', 'sub_cardapio', 'opcao',)
		read_only_fields = ('id',)