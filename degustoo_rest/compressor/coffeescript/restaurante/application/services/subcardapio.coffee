angular
	.module('RestauranteAPP')
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