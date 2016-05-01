angular
	.module('RestauranteAPP')
	.directive(
		'listaItemCardapio',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-item-cardapio.html'
			controller: 'itemCardapioController'
			controllerAs: 'item_cardapio_controller'
	)