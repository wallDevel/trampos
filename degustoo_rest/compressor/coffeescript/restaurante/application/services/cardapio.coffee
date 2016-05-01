angular
	.module('RestauranteAPP')
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