from django.template import Library

register = Library()

@register.inclusion_tag('restaurante/templatetags/card_list.html')
def card_list(restaurante):
	cardapios = restaurante.getEvery_menu()
	context = {'cardapios': cardapios}
	return context