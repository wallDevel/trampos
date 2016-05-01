angular
	.module('RestauranteAPP')	
	.directive(
		'listaItemSubcardapio',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-item-subcardapio.html'
			controller: 'itemSubcardapioController'
			controllerAs: 'item_subcardapio_controller'
	)