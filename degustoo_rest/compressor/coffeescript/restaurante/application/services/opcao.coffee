angular
	.module('RestauranteAPP')
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

			_getOpcao = (cardapio_id, opcao_id) ->
				$http(
					method: 'GET'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'+opcao_id+'/'
				)

			_editarOpcao = (cardapio_id, opcao_id, dados) ->
				$http(
					method: 'PUT'
					url: '/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'+opcao_id+'/'
					data: dados
				)

			_deletarOpcao = (cardapio_id, opcao_id) ->
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