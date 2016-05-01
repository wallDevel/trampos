angular
	.module('RestauranteAPP')
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