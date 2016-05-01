angular
	.module('RestauranteAPP')
	.directive(
		'listaCardapio',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-cardapio.html'
			controller: 'cardapioController'
			controllerAs: 'cardapio_controller'
	)