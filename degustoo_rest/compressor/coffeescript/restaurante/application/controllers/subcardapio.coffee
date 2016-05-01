angular
	.module('RestauranteAPP')
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