angular
	.module('RestauranteAPP')
	.directive(
		'listaItemOpcao',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-item-opcao.html'
			controller: 'itemOpcaoController'
			controllerAs: 'item_opcao_controller'
	)