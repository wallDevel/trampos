angular
	.module('RestauranteAPP', [])
	.config([
		'$httpProvider',
		'$interpolateProvider',
		($httpProvider, $interpolateProvider) ->
			$interpolateProvider.startSymbol('[[')
			$interpolateProvider.endSymbol(']]')
			$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
			$httpProvider.defaults.xsrfCookieName = 'csrftoken'
			return
	])
	.factory(
		'cardapioAJAX',
		($http) ->
			_novoCardapio = (restaurante_id, dados) ->
				$http(
					method: 'POST'
					url: '/ajax/restaurante/'+restaurante_id+'/cardapio/'
					data: dados
				)
			_listarCardapios = (restaurante_id) ->
				$http(
					method: 'GET'
					url: '/ajax/restaurante/'+restaurante_id+'/cardapio/'
				)
			_getCardapio = (restaurante_id, cardapio_id) ->
				$http(
					method: 'GET'
					url: '/ajax/restaurante/'+restaurante_id+'/cardapio/'+cardapio_id+'/'
				)
			_editarCardapio = (restarante_id, cardapio_id, dados) ->
				$http(
					method: 'PUT'
					url: '/ajax/restaurante/'+restaurante_id+'/cardapio/'+cardapio_id+'/'
					data: dados
				)
			_deletarCardapio = (restaurante_id, cardapio_id) ->
				$http(
					method: 'DELETE'
					url: '/ajax/restaurante/'+restaurante_id+'/cardapio/'+cardapio_id+'/'
				)
			novoCardapio: 		_novoCardapio
			listarCardapios: 	_listarCardapios
			getCardapio: 		_getCardapio
			editarCardapio: 	_editarCardapio
			deletarCardapio: 	_deletarCardapio
	)
	.factory(
		'subcardapioAJAX',
		($http) ->
			_novoSubcardapio = (cardapio_id, dados) ->
				$http(
					method: 'POST'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'
					data: dados
				)
			_listarSubcardapios = (cardapio_id) ->
				$http(
					method: 'GET'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'
				)
			_getSubcardapio = (cardapio_id, subcardapio_id) ->
				$http(
					method: 'GET'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'+subcardapio_id+'/'
				)
			_editarSubcardapio = (cardapio_id, subcardapio_id, dados) ->
				$http(
					method: 'PUT'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'+subcardapio_id+'/'
					data: dados
				)
			_deletarSubcardapio = (cardapio_id, subcardapio_id) ->
				$http(
					method: 'DELETE'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'+subcardapio_id+'/'
				)
			novoSubcardapio: 		_novoSubcardapio
			listarSubcardapios: 	_listarSubcardapios
			getSubcardapio: 		_getSubcardapio
			editarSubcardapio: 		_editarSubcardapio
			deletarSubcardapio: 	_deletarSubcardapio
	)
	.factory(
		'opcaoAJAX',
		($http) ->
			_novoOpcao = (cardapio_id, dados) ->
				$http(
					method: 'POST'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'
					data: dados
				)
			_listarOpcoes = (cardapio_id) ->
				$http(
					method: 'GET'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'
				)
			_getOpcao = (cardapio_id, cardapio_id) ->
				$http(
					method: 'GET'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'+opcao_id+'/'
				)
			_editarOpcao = (restarante_id, cardapio_id, dados) ->
				$http(
					method: 'PUT'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'+opcao_id+'/'
					data: dados
				)
			_deletarOpcao = (cardapio_id, cardapio_id) ->
				$http(
					method: 'DELETE'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'+opcao_id+'/'
				)
			novaOpcao: 		_novaOpcao
			listarOpcoes: 	_listarOpcoes
			getOpcao: 		_getOpcao
			editarOpcao: 	_editarOpcao
			deletarOpcao: 	_deletarOpcao
	)
	.factory(
		'itemCardapioAJAX',
		($http) ->
			_novoItem = (cardapio_id, dados) ->
				$http(
					method: 'POST'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/item/'
					data: dados
				)
			_listarItens = (cardapio_id) ->
				$http(
					method: 'GET',
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/item/'
				)
			_getItem = (cardapio_id, item_id) ->
				$http(
					method: 'GET',
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/item/'+item_id+'/'
				)
			_editarItem = (cardapio_id, item_id, dados) ->
				$http(
					method: 'PUT',
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/item/'+item_id+'/'
					data: dados
				)
			_deletarItem = (cardapio_id, item_id) ->
				$http(
					method: 'DELETE',
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/item/'+item_id+'/'
				)
			novoItem: 		_novoItem
			editarItem: 	_editarItem
			getItem: 		_getItem
			listarItens: 	_listarItens
			deletarItem: 	_deletarItem
	)
	.factory(
		'itemSubcardapioAJAX',
		($http) ->
			_novoItem = (subcardapio_id, dados) ->
				$http(
					method: 'POST'
					url: '/ajax/restaurante/subcardapio/'+subcardapio_id+'/item/'
					data: dados
				)
			_listarItens = (subcardapio_id) ->
				$http(
					method: 'GET',
					url: '/ajax/restaurante/subcardapio/'+subcardapio_id+'/item/'
				)
			_getItem = (subcardapio_id, item_id) ->
				$http(
					method: 'GET',
					url: '/ajax/restaurante/subcardapio/'+cardapio_id+'/item/'+item_id+'/'
				)
			_editarItem = (subcardapio_id, item_id, dados) ->
				$http(
					method: 'PUT',
					url: '/ajax/restaurante/subcardapio/'+subcardapio_id+'/item/'+item_id+'/'
					data: dados
				)
			_deletarItem = (subcardapio_id, item_id) ->
				$http(
					method: 'DELETE',
					url: '/ajax/restaurante/subcardapio/'+subcardapio_id+'/item/'+item_id+'/'
				)
			novoItem: 		_novoItem
			editarItem: 	_editarItem
			getItem: 		_getItem
			listarItens: 	_listarItens
			deletarItem: 	_deletarItem
	)
	.factory(
		'itemOpcaoAJAX',
		($http) ->
			_novoItem = (opcao_id, dados) ->
				$http(
					method: 'POST'
					url: '/ajax/restaurante/opcao/'+opcao_id+'/item/'
					data: dados
				)
			_listarItens = (opcao_id) ->
				$http(
					method: 'GET',
					url: '/ajax/restaurante/opcao/'+opcao_id+'/item/'
				)
			_getItem = (opcao_id, item_id) ->
				$http(
					method: 'GET',
					url: '/ajax/restaurante/opcao/'+opcao_id+'/item/'+item_id+'/'
				)
			_editarItem = (opcao_id, item_id, dados) ->
				$http(
					method: 'PUT',
					url: '/ajax/restaurante/opcao/'+opcao_id+'/item/'+item_id+'/'
					data: dados
				)
			_deletarItem = (opcao_id, item_id) ->
				$http(
					method: 'DELETE',
					url: '/ajax/restaurante/opcao/'+opcao_id+'/item/'+item_id+'/'
				)
			novoItem: 		_novoItem
			editarItem: 	_editarItem
			getItem: 		_getItem
			listarItens: 	_listarItens
			deletarItem: 	_deletarItem
	)
	.directives(
		'listaCardapio',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-cardapio.html'
			controller: 'cardapioController'
			controllerAs: 'cardapio_controller'
	)
	.directives(
		'listaSubcardapio',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-subcardapio.html'
			controller: 'subcardapioController'
			controllerAs: 'subcardapio_controller'
	)
	.directives(
		'listaOpcao',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-opcao.html'
			controller: 'opcaoController'
			controllerAs: 'opcao_controller'
	)
	.directives(
		'listaItemCardapio',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-item-cardapio.html'
			controller: 'itemCardapioController'
			controllerAs: 'item_cardapio_controller'
	)
	.directives(
		'listaItemSubcardapio',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-item-subcardapio.html'
			controller: 'itemSubcardapioController'
			controllerAs: 'item_subcardapio_controller'
	)
	.directives(
		'listaItemOpcao',
		->
			restrict: 'E'
			templateUrl: '/static/restaurante/js/application/templates/lista-item-opcao.html'
			controller: 'itemOpcaoController'
			controllerAs: 'item_opcao_controller'
	)
	.controller(
		'cardapioController',
		($scope, cardapioAJAX) ->
			reload = (restaurante_id) ->
				cardapioAJAX
					.listarCardapios(restaurante_id)
					.success(
						(data) ->
							$scope.lista_cardapio = data
							return
					)
				return
			this.novoCardapio = (restaurante_id, dados) ->
				cardapioAJAX
					.novoCardapio(restaurante_id, dados)
					.success(
						(data) ->
							reload restaurante_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.listarCardapios = (restaurante_id) ->
				cardapioAJAX
					.listarCardapios(restaurante_id)
					.success(
						(data) ->
							reload restaurante_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.getCardapio = (restaurante_id, cardapio_id) ->
				cardapioAJAX
					.getCardapio(resturante_id, cardapio_id)
					.success(
						(data) ->
							console.log data
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.editarCardapio = (restaurante_id, cardapio_id, dados) ->
				cardapioAJAX
					.editarCardapio(restaurante_id, cardapio_id, dados)
					.success(
						(data) ->
							reload restaurante_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.deletarCardapio = (restaurante_id, cardapio_id) ->
				cardapioAJAX
					.deletarCardapio(restaurante_id, cardapio_id)
					.success(
						(data) ->
							reload restaurante_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			return
	)
	.controller(
		'subcardapioController',
		($scope, subcardapioAJAX) ->
			reload = (cardapio_id) ->
				subcardapioAJAX
					.listarSubcardapios(cardapio_id)
					.success(
						$scope.lista_subcardapio = data
					)
				return
			this.novoSubcardapio = (cardapio_id, dados) ->
				subcardapioAJAX
					.novoSubcardapio(cardapio_id, dados)
					.success(
						(data) ->
							reload cardapio_id
					)
					.error(
						(data) ->
							console.log data
					)
				return
			this.listarSubcardapios = (cardapio_id) ->
				subcardapioAJAX
					.listarSubcardapios(cardapio_id)
					.success(
						(data) ->
							reload cardapio_id
					)
					.error(
						(data) ->
							console.log data
					)
				return
			this.getSubcardapio = (cardapio_id, subcardapio_id) ->
				subcardapioAJAX
					.getSubcardapio(cardapio_id, subcardapio_id)
					.success(
						(data) ->
							console.log data
					)
					.error(
						(data) ->
							console.log data
					)
				return
			this.editarSubcardapio = (cardapio_id, subcardapio_id, dados) ->
				subcardapioAJAX
					.editarSubcardapio(cardapio_id, subcardapio_id, dados)
					.success(
						(data) ->
							reload cardapio_id
					)
					.error(
						(data) ->
							console.log data
					)
				return
			this.deletarSubcardapio = (cardapio_id, subcardapio_id) ->
				subcardapioAJAX
					.deletarSubcardapio(cardapio_id, subcardapio_id)
					.success(
						(data) ->
							reload cardapio_id
					)
					.error(
						(data) ->
							console.log data
					)
				return
			return
	)
	.controller(
		'opcaoController',
		($scope, opcaoAJAX) ->
			reload = (cardapio_id) ->
				opcaoAJAX
					.listarOpcoes(cardapio_id)
					.success(
						$scope.lista_opcao = data
					)
				return
			this.novaOpcao = (cardapio_id, dados) ->
				opcaoAJAX
					.novaOpcao(cardapio_id, dados)
					.success(
						(data) ->
							reload cardapio_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.listarOpcoes = (cardapio_id) ->
				opcaoAJAX
					.listarOpcoes(cardapio_id)
					.success(
						(data) ->
							reload cardapio_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.getOpcao = (cardapio_id, opcao_id) ->
				opcaoAJAX
					.getOpcao(cardapio_id, opcao_id)
					.success(
						(data) ->
							console.log data
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.editarOpcao = (cardapio_id, opcao_id, dados) ->
				opcaoAJAX
					.editarOpcao(cardapio_id, opcao_id, dados)
					.success(
						(data) ->
							reload cardapio_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.deletarOpcao = (cardapio_id, opcao_id) ->
				opcaoAJAX
					.deletarOpcao(cardapio_id, opcao_id)
					.success(
						(data) ->
							reload cardapio_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			return
	)
	.controller(
		'itemCardapioController',
		($scope, itemCardapioAJAX) ->
			reload = (cardapio_id) ->
				itemCardapioAJAX
					.listarItens(cardapio_id)
					.success(
						(data) ->
							$scope.lista_item_cardapio = data
							$scope.novoItem.nome = ""
							$scope.novoItem.preco = ""
							return
					)
				return
			this.novoItem = (cardapio_id) ->
				itemCardapioAJAX
					.novoItem(cardapio_id)
					.success(
						(data) ->
							reload(cardapio_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.listarItens = (cardapio_id) ->
				itemCardapioAJAX
					.listarItens(cardapio_id)
					.success(
						(data) ->
							reload(cardapio_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.getItem = (cardapio_id, item_id) ->
				itemCardapioAJAX
					.getItem(cardapio_id, item_id)
					.success(
						(data) ->
							return
					)
					.error(
						(data) ->
							return
					)
				return
			this.editarItem = (cardapio_id, item_id, dados) ->
				itemCardapioAJAX
					.editarItem(cardapio_id, item_id, dados)
					.success(
						(data) ->
							return
					)
					.error(
						(data) ->
							return
					)
				return
			this.deletarItem = (cardapio_id, item_id) ->
				itemCardapioAJAX
					.deletarItem(cardapio_id, item_id)
					.success(
						(data) ->
							reload(cardapio_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			return
	)
	.controller(
		'itemSubcardapioController',
		($scope, itemSubcardapioAJAX) ->
			reload = (subcardapio_id) ->
				itemSubcardapioAJAX
					.listarItens(subcardapio_id)
					.success(
						(data) ->
							$scope.lista_item_subcardapio = data
							$scope.novoItem.nome = ""
							$scope.novoItem.preco = ""
							return
					)
				return
			this.novoItem = (subcardapio_id) ->
				itemSubcardapioAJAX
					.novoItem(subcardapio_id)
					.success(
						(data) ->
							reload(subcardapio_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.listarItens = (subcardapio_id) ->
				itemSubcardapioAJAX
					.listarItens(subcardapio_id)
					.success(
						(data) ->
							reload(subcardapio_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.getItem = (subcardapio_id, item_id) ->
				itemSubcardapioAJAX
					.getItem(subcardapio_id, item_id)
					.success(
						(data) ->
							return
					)
					.error(
						(data) ->
							return
					)
				return
			this.editarItem = (subcardapio_id, item_id, dados) ->
				itemSubcardapioAJAX
					.editarItem(subcardapio_id, item_id, dados)
					.success(
						(data) ->
							return
					)
					.error(
						(data) ->
							return
					)
				return
			this.deletarItem = (subcardapio_id, item_id) ->
				itemSubcardapioAJAX
					.deletarItem(subcardapio_id, item_id)
					.success(
						(data) ->
							reload(subcardapio_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			return
	)
	.controller(
		'itemOpcaoController',
		($scope, itemOpcaoAJAX) ->
			reload = (opcao_id) ->
				itemOpcaoAJAX
					.listarItens(opcao_id)
					.success(
						(data) ->
							$scope.lista_item_opcao = data
							$scope.novoItem.nome = ""
							$scope.novoItem.preco = ""
							return
					)
				return
			this.novoItem = (opcao_id) ->
				itemOpcaoAJAX
					.novoItem(opcao_id)
					.success(
						(data) ->
							reload(opcao_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.listarItens = (opcao_id) ->
				itemOpcaoAJAX
					.listarItens(opcao_id)
					.success(
						(data) ->
							reload(opcao_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.getItem = (opcao_id, item_id) ->
				itemOpcaoAJAX
					.getItem(opcao_id, item_id)
					.success(
						(data) ->
							return
					)
					.error(
						(data) ->
							return
					)
				return
			this.editarItem = (opcao_id, item_id, dados) ->
				itemOpcaoAJAX
					.editarItem(opcao_id, item_id, dados)
					.success(
						(data) ->
							return
					)
					.error(
						(data) ->
							return
					)
				return
			this.deletarItem = (opcao_id, item_id) ->
				itemOpcaoAJAX
					.deletarItem(opcao_id, item_id)
					.success(
						(data) ->
							reload(opcao_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			return
	)
