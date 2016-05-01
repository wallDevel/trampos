angular
	.module('RestauranteAPP')
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