angular
	.module('RestauranteAPP')
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