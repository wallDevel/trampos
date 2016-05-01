angular
	.module('RestauranteAPP')
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