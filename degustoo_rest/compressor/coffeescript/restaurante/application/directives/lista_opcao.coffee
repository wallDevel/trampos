angular
	.module('RestauranteAPP')
	.directive(
		'listaOpcao',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-opcao.html'
			controller: 'opcaoController'
			controllerAs: 'opcao_controller'
	)