angular
	.module('RestauranteAPP')
	.directive(
		'listaSubcardapio',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-subcardapio.html'
			controller: 'subcardapioController'
			controllerAs: 'subcardapio_controller'
	)