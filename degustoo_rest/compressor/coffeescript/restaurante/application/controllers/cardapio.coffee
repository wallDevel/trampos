angular
	.module('RestauranteAPP')
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