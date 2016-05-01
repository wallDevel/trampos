angular
	.module('RestauranteAPP')	
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