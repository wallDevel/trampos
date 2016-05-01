from django.template import Library

register = Library()

@register.inclusion_tag("restaurante/templatetags/item_list.html")
def item_list(cardapio):
	itens = cardapio.getEvery_item()
	context = {"cardapio": cardapio, "itens":itens}
	return context

@register.inclusion_tag("restaurante/templatetags/op_item_list.html")
def option_item_list(opcao):
	itens = opcao.getEvery_item()
	context = {'cardapio':opcao.cardapio,'opcao':opcao,'itens':itens}
	return context

@register.inclusion_tag("restaurante/templatetags/sub_item_list.html")
def sub_item_list(subcardapio):
	itens = subcardapio.getEvery_item()
	context = {'cardapio':subcardapio.cardapio,'subcardapio':subcardapio,'itens':itens}
	return context